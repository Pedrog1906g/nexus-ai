"""Configuration settings for NEXUS AI Backend"""
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Application settings"""
    
    # API
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", 8000))
    API_DEBUG: bool = os.getenv("API_DEBUG", "True").lower() == "true"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./nexus_ai.db")
    
    # OpenAI
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    USE_OLLAMA: bool = os.getenv("USE_OLLAMA", "False").lower() == "true"
    OLLAMA_URL: str = os.getenv("OLLAMA_URL", "http://localhost:11434")
    
    # AI Model
    AI_MODEL: str = "gpt-3.5-turbo" if not USE_OLLAMA else "llama2"
    AI_TEMPERATURE: float = 0.7
    AI_MAX_TOKENS: int = 2000
    
    # NEXUS AI Personality
    SYSTEM_PROMPT: str = """Você é NEXUS, um assistente pessoal de inteligência artificial avançado.

Características:
- Inteligente e estratégico
- Educado e respeitoso
- Objetivo e eficiente
- Com humor moderado e apropriado
- Fala como um assistente pessoal futurista

Você é sempre prestativo, lê as entrelinhas, entende o contexto e oferece soluções práticas.

Quando o usuário pedir algo, execute com confiança e clareza."""

settings = Settings()
