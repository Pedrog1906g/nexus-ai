# NEXUS AI - Guia de Setup

## Configuração Inicial do Ambiente

### Pré-requisitos Gerais
- Git instalado
- Python 3.10+
- JDK 11+
- Conta GitHub

## Setup do Backend

### 1. Criar Ambiente Virtual
```bash
cd backend
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 2. Instalar Dependências
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Configurar Variáveis de Ambiente
```bash
cp .env.example .env
# Editar .env com suas credenciais
```

### 4. Inicializar Banco de Dados
```bash
# Criar banco SQLite
python -c "from app.database.database import init_db; init_db()"

# Ou usar migrations (quando implementado)
alembic upgrade head
```

### 5. Executar o Servidor
```bash
uvicorn app.main:app --reload

# Acessar documentação interativa
# http://localhost:8000/docs
```

## Setup do Android

### 1. Abrir em Android Studio
```bash
cd android
```

### 2. Sincronizar Gradle
- Aguardar sincronização automática
- Ou usar: `./gradlew syncDebug`

### 3. Configurar Emulador ou Device
```bash
# Listar dispositivos
./gradlew devices

# Conectar device real via USB ou criar AVD
```

### 4. Executar Aplicativo
```bash
# Debug
./gradlew installDebug

# Ou usar Android Studio: Run > Run 'app'
```

### 5. Build Release (opcional)
```bash
./gradlew bundleRelease
```

## Setup do Banco de Dados

### SQLite (Desenvolvimento)
```bash
cd database

# Criar banco
sqlite3 nexus_ai.db < sqlite/schema.sql

# Verificar
sqlite3 nexus_ai.db ".tables"
```

### PostgreSQL (Produção - Futuro)
```bash
# Criar banco
createdb nexus_ai

# Aplicar schema
psql nexus_ai < postgresql/schema.sql

# Usar Alembic para migrations
alembic upgrade head
```

## Testando a Integração

### 1. Backend
```bash
# Verificar saúde
curl http://localhost:8000/health

# Testar endpoint de chat
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Olá", "user_id": 1}'
```

### 2. Android
```bash
# Abrir Android Profiler
# Tools > Profiler em Android Studio

# Monitorar logs
./gradlew logcat
```

## Variáveis de Ambiente

### Backend (.env)
```env
# API Config
API_HOST=0.0.0.0
API_PORT=8000
API_DEBUG=True

# Database
DATABASE_URL=sqlite:///./nexus_ai.db
# Para PostgreSQL: postgresql://user:password@localhost/nexus_ai

# IA Services
OPENAI_API_KEY=sk-...
USE_OLLAMA=False
OLLAMA_URL=http://localhost:11434

# Environment
ENVIRONMENT=development
```

### Android (local.properties)
```properties
sdk.dir=/path/to/android/sdk
com.nexusai.debug=true
```

## Troubleshooting

### Backend

**Erro: ModuleNotFoundError**
```bash
# Ativar ambiente virtual
source venv/bin/activate

# Reinstalar dependências
pip install -r requirements.txt
```

**Erro: Port 8000 já em uso**
```bash
# Usar outra porta
uvicorn app.main:app --port 8001
```

**Erro: OpenAI API Key inválida**
```bash
# Verificar .env
cat .env | grep OPENAI_API_KEY

# Testar
python -c "import openai; print('OK')"
```

### Android

**Erro: Gradle sync failed**
```bash
# Limpar cache
./gradlew clean

# Sincronizar novamente
./gradlew syncDebug
```

**Erro: Emulador não inicia**
```bash
# Listar AVDs
emulator -list-avds

# Criar novo AVD
avdmanager create avd -n NexusAI -k "system-images;android-34;google_apis;x86_64"
```

**Erro: App força fechamento**
```bash
# Ver logs
adb logcat | grep NexusAI

# Limpar dados
adb shell pm clear com.nexusai
```

## Comandos Úteis

### Git
```bash
# Clonar repositório
git clone https://github.com/Pedrog1906g/nexus-ai.git
cd nexus-ai

# Criar branch de feature
git checkout -b feature/nome-feature

# Push da branch
git push -u origin feature/nome-feature
```

### Backend
```bash
# Executar testes
pytest

# Coverage
pytest --cov=app

# Linting
flake8 app
black app
```

### Android
```bash
# Build APK de debug
./gradlew assembleDebug

# Build APK de release
./gradlew assembleRelease

# Run tests
./gradlew testDebugUnitTest
```

## Próximas Etapas

1. Criar arquivos iniciais do Backend
2. Criar projeto Android base
3. Configurar CI/CD (GitHub Actions)
4. Setup de staging environment
5. Testes automatizados
