"""Chat endpoints"""
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.schemas import ChatRequest, ChatResponse, MessageResponse
from app.services.ai_service import AIService
from app.services.conversation_service import ConversationService
from app.services.memory_service import MemoryService
from app.models.models import User

router = APIRouter(prefix="/api/v1", tags=["Chat"])


@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    """
    Send a message and get AI response
    
    - **user_id**: User ID
    - **conversation_id** (optional): Existing conversation ID
    - **message**: User message
    """
    
    # Verify user exists
    user = db.query(User).filter(User.id == request.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Create or get conversation
    if request.conversation_id:
        conversation = ConversationService.get_conversation(
            db, request.conversation_id
        )
        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found")
    else:
        conversation = ConversationService.create_conversation(
            db, request.user_id, "Nova Conversa"
        )
    
    # Add user message
    user_msg = ConversationService.add_message(
        db,
        conversation.id,
        "user",
        request.message
    )
    
    # Get conversation history (last 10 messages for context)
    history = ConversationService.get_conversation_messages(
        db, conversation.id, limit=10
    )
    
    # Build conversation context
    conv_history = [
        {"sender": msg.sender, "content": msg.content}
        for msg in history[:-1]  # Exclude current message
    ]
    
    # Get user context from memory
    user_context = MemoryService.get_user_context(db, request.user_id)
    
    # Generate AI response
    ai_response_text = AIService.generate_response(
        request.message,
        conversation_history=conv_history,
        user_context=user_context
    )
    
    # Add AI message
    ai_msg = ConversationService.add_message(
        db,
        conversation.id,
        "nexus",
        ai_response_text
    )
    
    # Return response
    return {
        "conversation_id": conversation.id,
        "user_message": {
            "id": user_msg.id,
            "sender": user_msg.sender,
            "content": user_msg.content,
            "conversation_id": user_msg.conversation_id,
            "timestamp": user_msg.timestamp
        },
        "ai_message": {
            "id": ai_msg.id,
            "sender": ai_msg.sender,
            "content": ai_msg.content,
            "conversation_id": ai_msg.conversation_id,
            "timestamp": ai_msg.timestamp
        }
    }


@router.get("/conversations/{user_id}")
async def get_conversations(
    user_id: int,
    db: Session = Depends(get_db)
):
    """Get all conversations for a user"""
    
    # Verify user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    conversations = ConversationService.get_user_conversations(db, user_id)
    return {"conversations": conversations}


@router.get("/conversation/{conversation_id}")
async def get_conversation(
    conversation_id: int,
    db: Session = Depends(get_db)
):
    """Get conversation details with messages"""
    
    conversation = ConversationService.get_conversation(db, conversation_id)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    
    messages = ConversationService.get_conversation_messages(
        db, conversation_id
    )
    
    return {
        "id": conversation.id,
        "user_id": conversation.user_id,
        "title": conversation.title,
        "created_at": conversation.created_at,
        "updated_at": conversation.updated_at,
        "messages": messages
    }


@router.delete("/conversation/{conversation_id}")
async def delete_conversation(
    conversation_id: int,
    db: Session = Depends(get_db)
):
    """Delete a conversation"""
    
    success = ConversationService.delete_conversation(db, conversation_id)
    if not success:
        raise HTTPException(status_code=404, detail="Conversation not found")
    
    return {"message": "Conversation deleted"}
