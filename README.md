# NEXUS AI - Assistente Pessoal IA 🤖

Um assistente pessoal inteligente inspirado no JARVIS para Android com IA, voz, memória e integração com dispositivos.

## ✨ Status: MVP Funcional ✅

**Backend:** ✅ FastAPI + SQLite + OpenAI  
**Android:** ✅ Jetpack Compose + Retrofit  
**Testes:** ✅ API testada e validada  

---

## 🚀 Quick Start

### Backend (30 segundos)
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
# API em: http://localhost:8000/docs
```

### Testar API
```bash
cd backend
python test_api.py
```

### Android
Abrir `android/` em Android Studio e rodar no emulador.

---

## 📱 O que funciona agora

✅ Chat com IA em tempo real  
✅ Histórico de conversas salvo  
✅ Sistema de memória do usuário  
✅ Interface futurista Material Design 3  
✅ API REST completa com 10+ endpoints  
✅ Suporte para OpenAI + Ollama (modelo local)  

---

## 🔗 Documentação Completa

- [**RUNNING.md**](RUNNING.md) - Como executar tudo
- [**STATUS.md**](STATUS.md) - Progresso do projeto
- [**ARCHITECTURE.md**](docs/ARCHITECTURE.md) - Arquitetura do sistema
- [**API Docs**](http://localhost:8000/docs) - Documentação interativa (quando rodando)

---

## 🎯 Fases Futuras

| Fase | Foco | Status |
|------|------|--------|
| 1 | Chat + API Base | ✅ Completo |
| 2 | Voz (STT/TTS) | ⏳ Próxima |
| 3 | Memória Avançada | ⏳ Planejada |
| 4 | Desktop App | ⏳ Planejada |
| 5 | Smart Home | ⏳ Planejada |
| 6 | Escalabilidade | ⏳ Planejada |

---

## 📊 Estrutura do Projeto

```
nexus-ai/
├── backend/              # API FastAPI
│   ├── app/
│   │   ├── models/       # SQLAlchemy models
│   │   ├── services/     # IA, Chat, Memory
│   │   ├── api/routes/   # Endpoints REST
│   │   └── main.py       # Entry point
│   ├── test_api.py       # Testes
│   └── requirements.txt
│
├── android/              # App Kotlin+Compose
│   ├── app/
│   │   ├── api/          # Retrofit client
│   │   ├── ui/           # Compose screens
│   │   └── viewmodel/    # MVVM logic
│   └── build.gradle.kts
│
├── database/             # Schemas SQL
├── docs/                 # Documentação
├── RUNNING.md            # Guia de execução
└── STATUS.md             # Status do projeto
```

---

## 🤖 Exemplo de Uso

```
Você: "Olá Nexus, qual é o seu nome?"

NEXUS: "Oi! Sou NEXUS, seu assistente pessoal de IA. 
        Estou aqui para te ajudar com tarefas, conversas 
        e manter você informado. Como posso ajudá-lo?"
```

---

## ⚙️ Tecnologias

**Backend**
- Python 3.10+
- FastAPI
- SQLAlchemy + SQLite
- OpenAI API + Ollama

**Android**
- Kotlin
- Jetpack Compose
- Material Design 3
- Retrofit + Coroutines

**IA**
- OpenAI GPT-3.5-turbo (ou local via Ollama)

---

## 🛠️ Próximos Passos

1. Adicionar Speech-to-Text (Whisper)
2. Adicionar Text-to-Speech
3. Botão de ativação por voz ("Ei Nexus")
4. Sistema avançado de memória com embeddings
5. Integração com Home Assistant

---

## 📝 Licença

MIT License - Sinta-se livre para usar e modificar!

---

## 👤 Autor

**Pedro Gentil**  
- GitHub: [@Pedrog1906g](https://github.com/Pedrog1906g)
- Email: seu-email-aqui

---

**NEXUS AI v0.1.0** - Seu assistente pessoal inteligente 🚀
