"""Pydantic schemas for request/response"""
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel


# User Schemas
class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


# Message Schemas
class MessageBase(BaseModel):
    sender: str  # 'user' ou 'nexus'
    content: str


class MessageCreate(MessageBase):
    pass


class MessageResponse(MessageBase):
    id: int
    conversation_id: int
    timestamp: datetime
    
    class Config:
        from_attributes = True


# Conversation Schemas
class ConversationBase(BaseModel):
    title: Optional[str] = None


class ConversationCreate(ConversationBase):
    pass


class ConversationResponse(ConversationBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class ConversationDetail(ConversationResponse):
    messages: List[MessageResponse] = []


# Memory Schemas
class MemoryBase(BaseModel):
    category: Optional[str] = None
    key: str
    value: str


class MemoryCreate(MemoryBase):
    pass


class MemoryResponse(MemoryBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


# Chat Schemas
class ChatRequest(BaseModel):
    user_id: int
    conversation_id: Optional[int] = None
    message: str


class ChatResponse(BaseModel):
    conversation_id: int
    user_message: MessageResponse
    ai_message: MessageResponse
    
    class Config:
        from_attributes = True


# Health Check
class HealthResponse(BaseModel):
    status: str
    environment: str
    ai_provider: str
