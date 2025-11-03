import os
from typing import Optional, Dict, Any
from service.api_service import call_api
from dotenv import load_dotenv
import logging

load_dotenv()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

NGUMZO_API_KEY = os.getenv("NGUMZO_API_KEY")
NGUMZO_API_URL = os.getenv("NGUMZO_API_URL", "https://ngumzo.com/v1")
NGUMZO_SENDER_ID = os.getenv("NGUMZO_SENDER_ID")

logger.info(f"✅ NGUMZO_API_URL: {NGUMZO_API_URL}")
logger.info(f"✅ NGUMZO_API_KEY: {'SET' if NGUMZO_API_KEY else 'NOT SET'}")
logger.info(f"✅ NGUMZO_SENDER_ID: {NGUMZO_SENDER_ID}")

class WhatsAppService:
    """Service for sending WhatsApp messages via Ngumzo API"""
    
    @staticmethod
    async def send_message(
        phone_number: str,
        message: str,
        message_type: str = "text"
    ) -> Dict[str, Any]:
        """
        Send a WhatsApp message using Ngumzo API
        
        Args:
            phone_number: Recipient's phone number (format: +254712345678)
            message: Message content
            message_type: Type of message ('text')
        
        Returns:
            API response with message status
        """
        
        try:
            # Normalize phone number
            phone_number = WhatsAppService._normalize_phone(phone_number)
            
            logger.debug(f"Sending WhatsApp message to: {phone_number}")
            logger.debug(f"Message: {message}")
            
            if not NGUMZO_API_KEY:
                return {
                    "success": False,
                    "error": "NGUMZO_API_KEY not found in environment variables"
                }
            
            # Ngumzo API expects this payload format
            payload = {
                "api_key": NGUMZO_API_KEY,
                "sender_id": NGUMZO_SENDER_ID,
                "to": phone_number,
                "message": message,
                "message_type": "text"
            }
            
            headers = {
                "Content-Type": "application/json"
            }
            
            # Use the correct endpoint: /send-message (not /messages)
            url = f"{NGUMZO_API_URL}/send-message"
            
            logger.debug(f"Full URL: {url}")
            logger.debug(f"Payload: {payload}")
            
            result = await call_api(
                url=url,
                method="POST",
                headers=headers,
                json=payload,
                timeout=30
            )
            
            logger.debug(f"API Response: {result}")
            return result
            
        except Exception as e:
            logger.error(f"Error sending WhatsApp message: {str(e)}")
            return {
                "success": False,
                "error": f"Exception: {str(e)}"
            }
    
    @staticmethod
    async def send_template_message(
        phone_number: str,
        template_name: str,
        parameters: Optional[list] = None
    ) -> Dict[str, Any]:
        """
        Send a template-based WhatsApp message
        """
        
        try:
            phone_number = WhatsAppService._normalize_phone(phone_number)
            
            logger.debug(f"Sending template '{template_name}' to {phone_number}")
            
            payload = {
                "api_key": NGUMZO_API_KEY,
                "sender_id": NGUMZO_SENDER_ID,
                "to": phone_number,
                "message_type": "template",
                "template_name": template_name,
                "parameters": parameters or []
            }
            
            headers = {
                "Content-Type": "application/json"
            }
            
            url = f"{NGUMZO_API_URL}/send-message"
            
            result = await call_api(
                url=url,
                method="POST",
                headers=headers,
                json=payload,
                timeout=30
            )
            
            return result
            
        except Exception as e:
            logger.error(f"Error sending template message: {str(e)}")
            return {
                "success": False,
                "error": f"Exception: {str(e)}"
            }
    
    @staticmethod
    async def send_media_message(
        phone_number: str,
        media_url: str,
        media_type: str = "image",
        caption: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send media (image, document, video) via WhatsApp
        """
        
        try:
            phone_number = WhatsAppService._normalize_phone(phone_number)
            
            logger.debug(f"Sending {media_type} to {phone_number}")
            
            payload = {
                "api_key": NGUMZO_API_KEY,
                "sender_id": NGUMZO_SENDER_ID,
                "to": phone_number,
                "message_type": media_type,
                "media_url": media_url,
                "caption": caption
            }
            
            headers = {
                "Content-Type": "application/json"
            }
            
            url = f"{NGUMZO_API_URL}/send-message"
            
            result = await call_api(
                url=url,
                method="POST",
                headers=headers,
                json=payload,
                timeout=30
            )
            
            return result
            
        except Exception as e:
            logger.error(f"Error sending media message: {str(e)}")
            return {
                "success": False,
                "error": f"Exception: {str(e)}"
            }
    
    @staticmethod
    def _normalize_phone(phone_number: str) -> str:
        """
        Normalize phone number to international format (+254...)
        """
        phone_number = phone_number.strip()
        
        # Remove any non-digit characters except +
        phone_number = ''.join(c for c in phone_number if c.isdigit() or c == '+')
        
        # Handle different formats
        if phone_number.startswith('0'):
            phone_number = '+254' + phone_number[1:]
        elif phone_number.startswith('254'):
            phone_number = '+' + phone_number
        elif not phone_number.startswith('+'):
            phone_number = '+' + phone_number
        
        return phone_number