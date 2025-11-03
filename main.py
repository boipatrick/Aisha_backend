from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator
import re
import os
from dotenv import load_dotenv
from service.api_service import call_api
from service.whatsapp_service import WhatsAppService
from database import SessionLocal, Base, engine, get_db
from models import WaitingList, WhatsAppMessage
from datetime import datetime

# Load environment variables
load_dotenv()

# Get Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

Base.metadata.create_all(bind=engine)

# ==================== Pydantic Models ====================

class WaitingListCreate(BaseModel):
    username: str
    phone_number: str

    @field_validator('phone_number')
    @classmethod
    def validate_phone(cls, v):
        # Matches formats like: 0712345678 or +25412345678
        pattern = r'^(?:254|\+254|0)\d{9}$'
        if not re.match(pattern, v):
            raise ValueError('Invalid Kenyan phone number format: 0712345678 or +254712345678')
        return v

    @field_validator('username')
    @classmethod
    def validate_username(cls, v):
        # Only letters, spaces and hyphens, 2-50 characters
        pattern = r'^[a-zA-Z\s-]{2,50}$'
        if not re.match(pattern, v):
            raise ValueError('Username must contain only letters, spaces, or hyphens (2-50 characters)')
        return v

class WhatsAppTextMessage(BaseModel):
    phone_number: str
    message: str

class WhatsAppTemplateMessage(BaseModel):
    phone_number: str
    template_name: str
    parameters: list = None

class WhatsAppMediaMessage(BaseModel):
    phone_number: str
    media_url: str
    media_type: str  # image, document, video, audio
    caption: str = None

class GeminiRequest(BaseModel):
    prompt: str

# ==================== FastAPI App ====================

app = FastAPI(title="Aisha Backend API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================== Waiting List Endpoints ====================

@app.post("/waiting-list/", response_model=dict)
async def create_waiting_list_item(item: WaitingListCreate, db=Depends(get_db)):
    """Add user to waiting list and send WhatsApp confirmation"""
    try:
        # Check if phone number already exists
        existing = db.query(WaitingList).filter(
            WaitingList.phone_number == item.phone_number
        ).first()
        
        if existing:
            raise HTTPException(status_code=400, detail="Phone number already in waiting list")
        
        db_item = WaitingList(**item.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        
        # Send WhatsApp confirmation message
        message = f"Hello {item.username}, 👋\n\nThanks for joining our waiting list! We'll notify you soon when we launch. 🚀"
        
        whatsapp_result = await WhatsAppService.send_message(
            phone_number=item.phone_number,
            message=message
        )
        
        return {
            "message": "Added to waiting list",
            "id": db_item.id,
            "whatsapp_sent": whatsapp_result.get("success", False)
        }
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

# ==================== WhatsApp Endpoints ====================

@app.post("/whatsapp/send-text")
async def send_whatsapp_text(request: WhatsAppTextMessage, db=Depends(get_db)):
    """Send a WhatsApp text message"""
    try:
        result = await WhatsAppService.send_message(
            phone_number=request.phone_number,
            message=request.message,
            message_type="text"
        )
        
        # Store in database
        if result.get("success"):
            db_message = WhatsAppMessage(
                phone_number=request.phone_number,
                message_content=request.message,
                message_type="text",
                status="sent",
                external_message_id=result.get("data", {}).get("messages", [{}])[0].get("id")
            )
            db.add(db_message)
            db.commit()
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/whatsapp/send-template")
async def send_whatsapp_template(request: WhatsAppTemplateMessage, db=Depends(get_db)):
    """Send a WhatsApp template message"""
    try:
        result = await WhatsAppService.send_template_message(
            phone_number=request.phone_number,
            template_name=request.template_name,
            parameters=request.parameters
        )
        
        if result.get("success"):
            db_message = WhatsAppMessage(
                phone_number=request.phone_number,
                message_content=f"Template: {request.template_name}",
                message_type="template",
                status="sent",
                external_message_id=result.get("data", {}).get("messages", [{}])[0].get("id")
            )
            db.add(db_message)
            db.commit()
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/whatsapp/send-media")
async def send_whatsapp_media(request: WhatsAppMediaMessage, db=Depends(get_db)):
    """Send a WhatsApp media message (image, video, document)"""
    try:
        result = await WhatsAppService.send_media_message(
            phone_number=request.phone_number,
            media_url=request.media_url,
            media_type=request.media_type,
            caption=request.caption
        )
        
        if result.get("success"):
            db_message = WhatsAppMessage(
                phone_number=request.phone_number,
                message_content=request.media_url,
                message_type=request.media_type,
                status="sent",
                external_message_id=result.get("data", {}).get("messages", [{}])[0].get("id")
            )
            db.add(db_message)
            db.commit()
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/whatsapp/messages/{phone_number}")
async def get_whatsapp_messages(phone_number: str, db=Depends(get_db)):
    """Get WhatsApp message history for a phone number"""
    try:
        messages = db.query(WhatsAppMessage).filter(
            WhatsAppMessage.phone_number == phone_number
        ).order_by(WhatsAppMessage.sent_at.desc()).all()
        
        return {"count": len(messages), "messages": messages}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ==================== Gemini Endpoints ====================

@app.post("/gemini")
async def get_gemini_response(request: GeminiRequest):
    """Get AI response from Gemini"""
    prompt = request.prompt
    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    result = await call_api(
        url=f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
        method="POST",
        headers={"Content-Type": "application/json"},
        json=payload
    )

    if not result["success"]:
        raise HTTPException(status_code=500, detail=result.get("error", "Unknown error"))

    data = result["data"]
    text = data["candidates"][0]["content"]["parts"][0]["text"]
    return {"response": text}

# ==================== Health Check ====================

@app.get("/")
def read_root():
    return {"message": "Aisha Backend API is running"}