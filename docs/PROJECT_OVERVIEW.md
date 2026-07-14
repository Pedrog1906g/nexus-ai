# NEXUS AI - Project Overview

Uma estrutura completa e bem documentada para o desenvolvimento do NEXUS AI, um assistente pessoal de IA para Android.

## 📁 Estrutura de Diretórios

- **`/android`** - Aplicativo Android (Kotlin + Jetpack Compose)
  - [README.md](/android/README.md) - Documentação do módulo Android
  - [INIT.md](/android/INIT.md) - Instruções de inicialização

- **`/backend`** - API REST (Python + FastAPI)
  - [README.md](/backend/README.md) - Documentação da API
  - `requirements.txt` - Dependências Python
  - `.env.example` - Variáveis de ambiente

- **`/database`** - Schemas de banco de dados
  - [README.md](/database/README.md) - Documentação de dados
  - `sqlite/schema.sql` - Schema SQLite

- **`/docs`** - Documentação do projeto
  - [ARCHITECTURE.md](/docs/ARCHITECTURE.md) - Arquitetura geral
  - [SETUP.md](/docs/SETUP.md) - Guia de configuração

- **`AI_INSTRUCTIONS.md`** - Instruções detalhadas de desenvolvimento
- **`README.md`** - Este arquivo

## 🎯 Objetivo

Criar um assistente pessoal de IA funcional para Android que:
- Comunica via chat com interface futurista
- Aceita entrada por voz (STT)
- Responde em voz (TTS)
- Mantém histórico de conversas
- Aprende e memoriza informações do usuário
- Tem personalidade própria inteligente e educada

## 🚀 Tecnologias

**Frontend (Android)**
- Kotlin
- Jetpack Compose
- Material Design 3
- Room Database

**Backend**
- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite → PostgreSQL

**IA**
- OpenAI API ou Ollama (local)

## 📋 Fases de Desenvolvimento

1. **FASE 1:** Estrutura Android + API básica
2. **FASE 2:** Integração com IA (OpenAI/Ollama)
3. **FASE 3:** Entrada por voz (STT)
4. **FASE 4:** Saída por voz (TTS)
5. **FASE 5:** Sistema de memória avançado
6. **FASE 6:** Integração com computador e IoT

## 🛠️ Quick Start

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

### Android
```bash
cd android
# Abrir em Android Studio
# Sincronizar Gradle
# Executar no emulador
```

### Banco de Dados
```bash
cd database
sqlite3 nexus_ai.db < sqlite/schema.sql
```

## 📚 Documentação

Consulte os arquivos README.md em cada diretório para informações detalhadas:

- [Android Setup](/android/README.md)
- [Backend Setup](/backend/README.md)
- [Database Setup](/database/README.md)
- [Arquitetura Completa](/docs/ARCHITECTURE.md)
- [Guia de Configuração](/docs/SETUP.md)

## 🔗 Links Importantes

- Repositório: https://github.com/Pedrog1906g/nexus-ai
- Issues: https://github.com/Pedrog1906g/nexus-ai/issues
- Documentação: Veja `/docs`

## 📝 Próximos Passos

1. ✅ Estrutura base criada
2. ⏳ Criar projeto Android em Android Studio
3. ⏳ Criar estrutura FastAPI
4. ⏳ Implementar endpoints iniciais
5. ⏳ Integração Android ↔ Backend
6. ⏳ Testes automatizados
7. ⏳ Deploy em staging

## 📧 Contato

**Desenvolvedor:** Pedro Gentil  
**Email:** seu-email-aqui  
**GitHub:** @Pedrog1906g

---

**NEXUS AI** - Seu assistente pessoal inteligente 🤖
