# NEXUS AI - Arquitetura

## Visão Geral
NEXUS AI é um assistente pessoal baseado em IA com três componentes principais: aplicativo Android, backend Python e banco de dados.

```
┌─────────────────────────────────────────────────────────────┐
│                     NEXUS AI Architecture                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────────┐         ┌──────────────────┐        │
│  │   Android App    │         │   Backend API    │        │
│  │   (Kotlin +      │◄───────►│   (FastAPI +     │        │
│  │   Jetpack        │ HTTP/S  │    Python)       │        │
│  │   Compose)       │         │                  │        │
│  └──────────────────┘         └──────────────────┘        │
│         │                              │                   │
│         │                              │                   │
│         └──────────────┬───────────────┘                   │
│                        │                                   │
│                        ▼                                   │
│              ┌──────────────────┐                         │
│              │   Database       │                         │
│              │   (SQLite/       │                         │
│              │    PostgreSQL)   │                         │
│              └──────────────────┘                         │
│                                                             │
│  ┌──────────────────────────────────────────────┐         │
│  │  AI Services (OpenAI API / Ollama)           │         │
│  │  External APIs & Integrations                │         │
│  └──────────────────────────────────────────────┘         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Componentes

### 1. Android App (`/android`)
- **Responsabilidade:** Interface do usuário, captura de voz, exibição de respostas
- **Tecnologias:** Kotlin, Jetpack Compose, Material Design 3
- **Comunicação:** HTTP/S com Backend API
- **Armazenamento Local:** Room Database (SQLite)

**Fluxo:**
1. Usuário entra por voz ou texto
2. App envia para Backend
3. Recebe resposta do Backend
4. Sintetiza em voz (TTS)
5. Armazena no histórico local

### 2. Backend API (`/backend`)
- **Responsabilidade:** Lógica de negócio, processamento de IA, gerenciamento de dados
- **Tecnologias:** FastAPI, Python, SQLAlchemy
- **Comunicação:** HTTP/S REST API
- **IA:** OpenAI API ou Ollama (local)

**Fluxo:**
1. Recebe requisição do App
2. Processa com OpenAI/Ollama
3. Gerencia memória do usuário
4. Armazena conversa no banco
5. Retorna resposta

### 3. Database (`/database`)
- **Responsabilidade:** Persistência de dados
- **Desenvolvimento:** SQLite
- **Produção:** PostgreSQL
- **Dados:** Usuários, conversas, memória, configurações

## Fluxo de Dados Principal

```
Usuário diz: "Qual é o meu nome?"
       │
       ▼
[Android App]
  • Captura áudio (STT)
  • Envia: {"message": "Qual é o meu nome?"}
       │
       ▼
[Backend API]
  • Recebe mensagem
  • Consulta memória local do usuário
  • Envia para OpenAI/Ollama com contexto
  • Gera resposta
  • Armazena em BD
       │
       ▼
[Android App]
  • Recebe resposta
  • Sintetiza voz (TTS)
  • Exibe no chat
  • Armazena localmente
       │
       ▼
Usuário ouve: "Seu nome é Pedro!"
```

## Segurança

### Android
- Validação de input
- HTTPS obrigatório
- Armazenamento seguro de tokens
- Permissões minimais

### Backend
- Autenticação com JWT
- Rate limiting
- Validação de schemas (Pydantic)
- SQL Injection prevention (ORM)
- CORS configurado

### Database
- Backup automático
- Criptografia de dados sensíveis
- Auditoria de acessos

## Performance

### Caching
- Cache de respostas comuns no Backend
- Cache de memória do usuário
- Cache local no App

### Otimizações
- Índices em tabelas principais
- Paginação de histórico
- Compressão de dados em trânsito
- Lazy loading de conversas

## Escalabilidade

### Fase Atual (MVP)
- Servidor único
- SQLite com sincronização
- Chamadas síncronas

### Futuro
- Load balancing
- PostgreSQL
- Redis para cache distribuído
- Fila de jobs assíncrona
- Microsserviços por domínio

## Fases de Implementação

### FASE 1: MVP
- [x] Estrutura base
- [ ] Interface Android básica
- [ ] Endpoints de chat no Backend
- [ ] Banco SQLite

### FASE 2: Voz e IA
- [ ] STT (Speech-to-Text)
- [ ] TTS (Text-to-Speech)
- [ ] Integração com OpenAI

### FASE 3: Memória
- [ ] Sistema de memória persistente
- [ ] Contexto nas respostas

### FASE 4: Expansão
- [ ] Autenticação avançada
- [ ] Integração com APIs externas
- [ ] Suporte a múltiplos idiomas

### FASE 5: Escala
- [ ] Preparação para produção
- [ ] Migração para PostgreSQL
- [ ] Deployment

## Decisões Arquiteturais

1. **Kotlin + Jetpack Compose:** Moderno, conciso, melhor suporte Google
2. **FastAPI:** Performance, documentação automática, suporte async
3. **SQLite → PostgreSQL:** Simplicidade no início, escalabilidade depois
4. **OpenAI/Ollama:** Flexibilidade entre cloud e local
5. **REST:** Simplicidade, fácil debug, padrão da indústria

## Próximos Passos

1. Criar estrutura base do Android
2. Criar estrutura base do Backend
3. Implementar endpoints iniciais
4. Testes end-to-end
5. Deploy em staging
