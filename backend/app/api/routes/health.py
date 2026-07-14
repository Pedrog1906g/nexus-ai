"""Health check endpoints"""
from fastapi import APIRouter
from app.config import settings
from app.schemas.schemas import HealthResponse

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    ai_provider = "Ollama" if settings.USE_OLLAMA else "OpenAI"
    return {
        "status": "healthy",
        "environment": settings.ENVIRONMENT,
        "ai_provider": ai_provider
    }


@router.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "NEXUS AI Backend API",
        "version": "0.1.0",
        "docs": "/docs"
    }
