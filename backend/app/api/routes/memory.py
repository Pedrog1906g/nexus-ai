"""Memory endpoints"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.schemas import MemoryCreate, MemoryResponse
from app.services.memory_service import MemoryService
from app.models.models import User, Memory

router = APIRouter(prefix="/api/v1", tags=["Memory"])


@router.post("/memory", response_model=MemoryResponse)
async def add_memory(
    memory: MemoryCreate,
    user_id: int,
    db: Session = Depends(get_db)
):
    """Add or update a memory entry"""
    
    # Verify user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    new_memory = MemoryService.add_memory(
        db,
        user_id,
        memory.key,
        memory.value,
        memory.category or "general"
    )
    
    return new_memory


@router.get("/memory/{user_id}")
async def get_user_memories(
    user_id: int,
    db: Session = Depends(get_db)
):
    """Get all memories for a user"""
    
    # Verify user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    memories = MemoryService.get_user_memories(db, user_id)
    return {"memories": memories}


@router.delete("/memory/{user_id}/{key}")
async def delete_memory(
    user_id: int,
    key: str,
    db: Session = Depends(get_db)
):
    """Delete a memory entry"""
    
    # Verify user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    success = MemoryService.delete_memory(db, user_id, key)
    if not success:
        raise HTTPException(status_code=404, detail="Memory not found")
    
    return {"message": "Memory deleted"}
