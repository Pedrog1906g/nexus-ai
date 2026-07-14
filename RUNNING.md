# 🚀 NEXUS AI - Como Executar

## Backend + Android + Testes

### ⚙️ Pré-requisitos
- Android Studio (com Kotlin)
- Python 3.10+
- Git
- JDK 11+

---

## 🔧 1. Backend (FastAPI)

### Iniciar API

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou venv\Scripts\activate  # Windows

pip install -r requirements.txt

# Configurar .env (já existe na pasta)
# Se precisar usar OpenAI, adicione sua chave em backend/.env

# Iniciar servidor
uvicorn app.main:app --reload

# API estará em: http://localhost:8000
# Docs Swagger: http://localhost:8000/docs
```

### Testar API

```bash
cd backend
source venv/bin/activate
python test_api.py
```

**Resultado esperado:**
```
✅ Health Check... ✅
✅ User Creation... ✅
✅ Add Memory... ✅
💬 Chat... ✅
📖 Get Conversation... ✅
```

---

## 📱 2. App Android

### Opção A: Android Studio (Recomendado)

1. **Abrir o projeto**
   ```bash
   # No Android Studio:
   # File > Open > nexus-ai/android
   ```

2. **Sincronizar Gradle**
   - Aguarde a sincronização automática
   - Ou: Build > Rebuild Project

3. **Rodar no Emulador**
   - AVD Manager > Create Virtual Device (API 24+)
   - Run > Run 'app'

### Opção B: Linha de Comando

```bash
cd android

# Build Debug
./gradlew assembleDebug

# Install no emulador/device
./gradlew installDebug

# Rodar direto
./gradlew runDebug
```

---

## 🧪 3. Testar Integração Completa

### Fluxo de Teste

1. **Backend rodando**
   ```bash
   # Terminal 1
   cd backend
   source venv/bin/activate
   uvicorn app.main:app --reload
   ```

2. **App Android rodando**
   - Emulador ligado e app instalado

3. **Testar no App**
   - Digitar mensagem: "Olá Nexus, qual é o seu nome?"
   - Nexus responde (com IA real ou erro de API key)

---

## 📊 Arquitetura da Integração

```
Android App (Jetpack Compose)
    ↓
Retrofit Client (HTTP)
    ↓
Backend API (FastAPI)
    ↓
SQLite Database
    ↓
OpenAI API (opcional)
```

---

## 🔑 Configurações Importantes

### Backend (.env)
```env
OPENAI_API_KEY=sk-seu-api-key-aqui
DATABASE_URL=sqlite:///./nexus_ai.db
USE_OLLAMA=False  # Mudar para True se usar modelo local
ENVIRONMENT=development
```

### Android (app/build.gradle.kts)
```kotlin
defaultConfig {
    minSdk = 24  // Mínimo suportado
    targetSdk = 34  // Máximo testado
}
```

---

## 🐛 Troubleshooting

### Backend

**Erro: ModuleNotFoundError**
```bash
pip install -r requirements.txt
```

**Erro: Port 8000 em uso**
```bash
lsof -i :8000
kill -9 <PID>
# Ou usar outra porta:
uvicorn app.main:app --port 8001
```

### Android

**Erro: Gradle sync failed**
```bash
./gradlew clean
./gradlew syncDebug
```

**Erro: App não se conecta ao Backend**
- Verifique se emulador está em `10.0.2.2:8000`
- Device físico: use IP da máquina em vez de localhost
- Check firewall permissions

**Erro: "Cannot resolve symbol"**
```bash
./gradlew build --info
```

---

## 📚 Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | /health | Status da API |
| POST | /api/v1/users | Criar usuário |
| GET | /api/v1/users/{id} | Obter usuário |
| POST | /api/v1/chat | Enviar mensagem |
| GET | /api/v1/conversations/{user_id} | Listar conversas |
| GET | /api/v1/conversation/{id} | Detalhes conversa |
| POST | /api/v1/memory | Adicionar memória |
| GET | /api/v1/memory/{user_id} | Listar memórias |

---

## 📖 Documentação da API

Após iniciar o Backend, acesse:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

---

## 🎯 Próximas Funcionalidades

- [ ] Adicionar reconhecimento de voz (STT)
- [ ] Adicionar síntese de voz (TTS)
- [ ] Sistema de memória avançado
- [ ] Autenticação biométrica
- [ ] Integração com casa inteligente
- [ ] Suporte para múltiplos idiomas

---

## 💡 Tips

1. **Testar API sem Android:**
   ```bash
   curl http://localhost:8000/health
   ```

2. **Resetar banco de dados:**
   ```bash
   cd backend
   rm -f nexus_ai.db
   python -c "from app.database.database import init_db; init_db()"
   ```

3. **Ver logs do Android:**
   ```bash
   adb logcat | grep NexusAI
   ```

4. **Usar Ollama local em vez de OpenAI:**
   - Instalar Ollama: https://ollama.ai
   - Em `.env`: `USE_OLLAMA=True`
   - Backend usará modelo local automaticamente

---

## 🚀 Deploy

### Staging
```bash
# Backend em produção
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Android build release
./gradlew bundleRelease
```

### Production
- Usar PostgreSQL em vez de SQLite
- Adicionar autenticação JWT
- HTTPS obrigatório
- Rate limiting
- CI/CD com GitHub Actions

---

**NEXUS AI v0.1.0** 🤖 | Backend ✅ | Android ✅ | Pronto para Testes ✅
