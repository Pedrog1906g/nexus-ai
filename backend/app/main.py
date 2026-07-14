"""Main application entry point"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import init_db
from app.api.routes import health, chat, user, memory
from app.config import settings

# Initialize database
init_db()

# Create FastAPI app
app = FastAPI(
    title="NEXUS AI Backend",
    description="Personal AI Assistant API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(health.router)
app.include_router(chat.router)
app.include_router(user.router)
app.include_router(memory.router)


@app.on_event("startup")
async def startup_event():
    """Initialize on startup"""
    print("🚀 NEXUS AI Backend starting...")
    print(f"Environment: {settings.ENVIRONMENT}")
    print(f"AI Provider: {'Ollama' if settings.USE_OLLAMA else 'OpenAI'}")


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "app.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.API_DEBUG
    )
