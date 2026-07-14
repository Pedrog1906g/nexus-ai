"""AI Service - Integration with OpenAI or Ollama"""
import os
from typing import Optional
from app.config import settings

# Conditional imports based on AI provider
if not settings.USE_OLLAMA:
    try:
        import openai
        openai.api_key = settings.OPENAI_API_KEY
    except ImportError:
        pass


class AIService:
    """Service for AI processing"""
    
    @staticmethod
    def generate_response(
        user_message: str,
        conversation_history: Optional[list] = None,
        user_context: Optional[str] = None
    ) -> str:
        """
        Generate AI response
        
        Args:
            user_message: User input message
            conversation_history: List of previous messages
            user_context: User information for personalization
            
        Returns:
            AI response text
        """
        
        # Build conversation context
        messages = [
            {
                "role": "system",
                "content": settings.SYSTEM_PROMPT + (f"\n\nUser Context: {user_context}" if user_context else "")
            }
        ]
        
        # Add conversation history
        if conversation_history:
            for msg in conversation_history:
                messages.append({
                    "role": msg.get("sender", "user"),
                    "content": msg.get("content", "")
                })
        
        # Add current user message
        messages.append({
            "role": "user",
            "content": user_message
        })
        
        try:
            if settings.USE_OLLAMA:
                return AIService._get_ollama_response(messages)
            else:
                return AIService._get_openai_response(messages)
        except Exception as e:
            return f"Desculpe, houve um erro ao processar sua solicitação: {str(e)}"
    
    @staticmethod
    def _get_openai_response(messages: list) -> str:
        """Get response from OpenAI API"""
        try:
            from openai import OpenAI
            
            client = OpenAI(api_key=settings.OPENAI_API_KEY)
            
            response = client.chat.completions.create(
                model=settings.AI_MODEL,
                messages=messages,
                temperature=settings.AI_TEMPERATURE,
                max_tokens=settings.AI_MAX_TOKENS
            )
            
            return response.choices[0].message.content.strip()
        except ImportError:
            return "Erro: OpenAI client não disponível. Instale: pip install openai"
        except Exception as e:
            return f"Erro OpenAI: {str(e)}"
    
    @staticmethod
    def _get_ollama_response(messages: list) -> str:
        """Get response from Ollama (local model)"""
        try:
            import requests
            import json
            
            # Format messages for Ollama
            formatted_messages = "\n".join([
                f"{msg['role'].upper()}: {msg['content']}"
                for msg in messages
            ])
            
            response = requests.post(
                f"{settings.OLLAMA_URL}/api/generate",
                json={
                    "model": settings.AI_MODEL,
                    "prompt": formatted_messages,
                    "stream": False,
                    "temperature": settings.AI_TEMPERATURE,
                },
                timeout=60
            )
            
            if response.status_code == 200:
                return response.json().get("response", "").strip()
            else:
                return f"Erro Ollama: {response.status_code}"
        except Exception as e:
            return f"Erro ao conectar com Ollama: {str(e)}"
