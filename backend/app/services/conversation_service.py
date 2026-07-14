"""Conversation Service"""
from sqlalchemy.orm import Session
from app.models.models import Conversation, Message, User
from app.schemas.schemas import ConversationCreate, MessageCreate


class ConversationService:
    """Service for conversation management"""
    
    @staticmethod
    def create_conversation(
        db: Session,
        user_id: int,
        title: str = None
    ) -> Conversation:
        """Create a new conversation"""
        conversation = Conversation(
            user_id=user_id,
            title=title or f"Conversa {Conversation.id}"
        )
        db.add(conversation)
        db.commit()
        db.refresh(conversation)
        return conversation
    
    @staticmethod
    def get_conversation(db: Session, conversation_id: int) -> Conversation:
        """Get conversation by ID"""
        return db.query(Conversation).filter(
            Conversation.id == conversation_id
        ).first()
    
    @staticmethod
    def get_user_conversations(db: Session, user_id: int) -> list:
        """Get all conversations for a user"""
        return db.query(Conversation).filter(
            Conversation.user_id == user_id
        ).order_by(Conversation.created_at.desc()).all()
    
    @staticmethod
    def add_message(
        db: Session,
        conversation_id: int,
        sender: str,
        content: str
    ) -> Message:
        """Add a message to conversation"""
        message = Message(
            conversation_id=conversation_id,
            sender=sender,
            content=content
        )
        db.add(message)
        db.commit()
        db.refresh(message)
        return message
    
    @staticmethod
    def get_conversation_messages(
        db: Session,
        conversation_id: int,
        limit: int = 50
    ) -> list:
        """Get messages from conversation"""
        return db.query(Message).filter(
            Message.conversation_id == conversation_id
        ).order_by(Message.timestamp.asc()).limit(limit).all()
    
    @staticmethod
    def delete_conversation(db: Session, conversation_id: int) -> bool:
        """Delete a conversation"""
        conversation = ConversationService.get_conversation(db, conversation_id)
        if conversation:
            db.delete(conversation)
            db.commit()
            return True
        return False
