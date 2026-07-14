# NEXUS AI - Database

## Visão Geral
Schemas de banco de dados para NEXUS AI, com preparação inicial em SQLite e migração futura para PostgreSQL.

## Estrutura de Banco de Dados

### Tabelas Principais

#### users
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### conversations
```sql
CREATE TABLE conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

#### messages
```sql
CREATE TABLE messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conversation_id INTEGER NOT NULL,
    sender VARCHAR(50) NOT NULL,  -- 'user' ou 'nexus_ai'
    content TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (conversation_id) REFERENCES conversations(id)
);
```

#### memory
```sql
CREATE TABLE memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    category VARCHAR(100),  -- 'preferences', 'personal_info', 'facts'
    key VARCHAR(255),
    value TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

#### settings
```sql
CREATE TABLE settings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    setting_key VARCHAR(255),
    setting_value TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

## Fases de Desenvolvimento

### FASE 1: Schema SQLite Básico
- [ ] Criar tabelas principais (users, conversations, messages)
- [ ] Definir relacionamentos
- [ ] Criar índices para performance

### FASE 2: Tabelas de Memória
- [ ] Criar tabela memory
- [ ] Adicionar tabela settings
- [ ] Implementar soft deletes

### FASE 3: Auditoria
- [ ] Adicionar campos de auditoria
- [ ] Criar tabela de logs
- [ ] Implementar triggers

### FASE 4: Migração para PostgreSQL
- [ ] Adaptação dos schemas
- [ ] Setup de Alembic
- [ ] Scripts de migração

### FASE 5: Otimizações
- [ ] Particionamento de dados
- [ ] Materialized views
- [ ] Índices avançados

## Diretórios

```
database/
├── sqlite/
│   ├── schema.sql
│   └── migrations/
├── postgresql/
│   ├── schema.sql
│   └── migrations/
├── alembic/  (para versionamento)
│   ├── versions/
│   └── env.py
└── README.md
```

## Como Usar

### SQLite (Desenvolvimento)
```bash
# Executar schema
sqlite3 nexus_ai.db < sqlite/schema.sql

# Verificar tabelas
sqlite3 nexus_ai.db ".tables"
```

### PostgreSQL (Produção)
```bash
# Criar banco
createdb nexus_ai

# Executar schema
psql nexus_ai < postgresql/schema.sql
```

## Próximos Passos
Criar os arquivos SQL com schemas e scripts de inicialização.
