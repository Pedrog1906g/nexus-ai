"""Memory Service"""
from sqlalchemy.orm import Session
from app.models.models import Memory


class MemoryService:
    """Service for user memory management"""
    
    @staticmethod
    def add_memory(
        db: Session,
        user_id: int,
        key: str,
        value: str,
        category: str = "general"
    ) -> Memory:
        """Add a memory entry"""
        # Check if memory with key already exists
        existing = db.query(Memory).filter(
            Memory.user_id == user_id,
            Memory.key == key
        ).first()
        
        if existing:
            existing.value = value
            existing.category = category
            db.commit()
            db.refresh(existing)
            return existing
        
        memory = Memory(
            user_id=user_id,
            key=key,
            value=value,
            category=category
        )
        db.add(memory)
        db.commit()
        db.refresh(memory)
        return memory
    
    @staticmethod
    def get_memory(db: Session, user_id: int, key: str) -> Memory:
        """Get specific memory entry"""
        return db.query(Memory).filter(
            Memory.user_id == user_id,
            Memory.key == key
        ).first()
    
    @staticmethod
    def get_user_memories(db: Session, user_id: int) -> list:
        """Get all memories for user"""
        return db.query(Memory).filter(
            Memory.user_id == user_id
        ).all()
    
    @staticmethod
    def get_user_context(db: Session, user_id: int) -> str:
        """Build context string from user memories"""
        memories = MemoryService.get_user_memories(db, user_id)
        if not memories:
            return ""
        
        context_parts = []
        for memory in memories:
            context_parts.append(f"{memory.key}: {memory.value}")
        
        return "\n".join(context_parts)
    
    @staticmethod
    def delete_memory(db: Session, user_id: int, key: str) -> bool:
        """Delete a memory entry"""
        memory = MemoryService.get_memory(db, user_id, key)
        if memory:
            db.delete(memory)
            db.commit()
            return True
        return False
