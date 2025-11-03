from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class WaitingList(Base):
    __tablename__ = "waiting_list"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    phone_number = Column(String, index=True)


class WhatsAppMessage(Base):
    """Track WhatsApp messages sent"""
    __tablename__ = "whatsapp_messages"
    
    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, index=True)
    message_content = Column(String)
    message_type = Column(String, default="text")
    status = Column(String, default="pending")  # pending, sent, delivered, failed
    external_message_id = Column(String, nullable=True)
    sent_at = Column(DateTime, default=datetime.utcnow)
    error_message = Column(String, nullable=True)