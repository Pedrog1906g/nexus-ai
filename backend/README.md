# NEXUS AI - Backend API

## Visão Geral
API REST desenvolvida com FastAPI (Python) que fornece inteligência artificial, processamento de linguagem natural e gerenciamento de memória para o NEXUS AI.

## Tecnologias
- **Framework:** FastAPI
- **Linguagem:** Python 3.10+
- **Banco de Dados:** SQLite (dev) → PostgreSQL (prod)
- **IA:** OpenAI API ou Ollama (local)
- **ORM:** SQLAlchemy
- **Async:** AsyncIO + Uvicorn

## Estrutura de Diretórios
```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── dependencies.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── conversation.py
│   │   ├── memory.py
│   │   └── user.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── conversation.py
│   │   └── memory.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── chat.py
│   │   ├── memory.py
│   │   └── health.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── ai_service.py
│   │   ├── memory_service.py
│   │   └── conversation_service.py
│   └── database/
│       ├── __init__.py
│       ├── database.py
│       └── models.py
├── tests/
├── requirements.txt
├── .env.example
└── main.py
```

## Endpoints Planejados

### Saúde
- `GET /health` - Verificar status da API

### Chat
- `POST /api/v1/chat` - Enviar mensagem
- `GET /api/v1/chat/history` - Obter histórico
- `GET /api/v1/chat/{conversation_id}` - Obter conversa específica

### Memória
- `POST /api/v1/memory` - Adicionar memória
- `GET /api/v1/memory` - Listar memórias
- `PUT /api/v1/memory/{memory_id}` - Atualizar memória
- `DELETE /api/v1/memory/{memory_id}` - Deletar memória

## Fases de Desenvolvimento

### FASE 1: Setup e Endpoints Básicos
- [ ] Criar estrutura FastAPI
- [ ] Configurar banco de dados SQLite
- [ ] Implementar endpoints de health check
- [ ] Criar schemas básicos

### FASE 2: Integração com IA
- [ ] Configurar OpenAI API ou Ollama
- [ ] Implementar serviço de IA
- [ ] Criar endpoint de chat
- [ ] Histórico de conversas

### FASE 3: Sistema de Memória
- [ ] Definir modelo de memória
- [ ] Endpoints CRUD
- [ ] Integrar memória nas respostas

### FASE 4: Autenticação
- [ ] Implementar JWT
- [ ] Rotas protegidas
- [ ] Gerenciamento de sessão

### FASE 5: Performance e Escala
- [ ] Caching com Redis
- [ ] Rate limiting
- [ ] Migrations com Alembic
- [ ] PostgreSQL em produção

## Como Executar

### Pré-requisitos
- Python 3.10+
- pip ou poetry

### Setup Inicial
```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Copiar variáveis de ambiente
cp .env.example .env
```

### Executar API
```bash
# Development (com reload automático)
uvicorn app.main:app --reload

# Production
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### API estará disponível em:
- **API:** http://localhost:8000
- **Docs Swagger:** http://localhost:8000/docs
- **Docs ReDoc:** http://localhost:8000/redoc

## Dependências Principais
- fastapi
- uvicorn[standard]
- sqlalchemy
- alembic
- python-dotenv
- openai (ou ollama)
- pydantic
- pytest

## Variáveis de Ambiente
```
OPENAI_API_KEY=seu_api_key_aqui
DATABASE_URL=sqlite:///./nexus_ai.db
ENVIRONMENT=development
```

## Próximos Passos
Criar arquivos iniciais do projeto FastAPI com estrutura base e requirements.txt.
