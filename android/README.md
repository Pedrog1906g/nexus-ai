# NEXUS AI - Módulo Android

## Visão Geral
Aplicativo Android nativo desenvolvido em Kotlin com Jetpack Compose, implementando uma interface futurista para o assistente pessoal NEXUS AI.

## Tecnologias
- **Linguagem:** Kotlin
- **IDE:** Android Studio
- **UI Framework:** Jetpack Compose
- **Design System:** Material Design 3
- **Arquitetura:** MVVM + Clean Architecture

## Estrutura de Diretórios
```
android/
├── app/
│   ├── src/
│   │   ├── main/
│   │   │   ├── kotlin/
│   │   │   │   └── com/nexusai/
│   │   │   │       ├── ui/
│   │   │   │       ├── viewmodel/
│   │   │   │       ├── repository/
│   │   │   │       ├── data/
│   │   │   │       └── NexusAIApp.kt
│   │   │   ├── res/
│   │   │   └── AndroidManifest.xml
│   │   └── test/
│   └── build.gradle.kts
├── build.gradle.kts
└── settings.gradle.kts
```

## Fases de Desenvolvimento

### FASE 1: Setup e Interface Básica
- [ ] Criar projeto Android em Kotlin
- [ ] Implementar UI de chat com Jetpack Compose
- [ ] Criar temas Material Design 3
- [ ] Implementar histórico de conversas em RecyclerView/LazyColumn

### FASE 2: Comunicação com Backend
- [ ] Setup de Retrofit/OkHttp
- [ ] Criar serviços de API
- [ ] Implementar autenticação
- [ ] Consumir endpoints da API FastAPI

### FASE 3: Entrada por Voz
- [ ] Integrar Speech-to-Text (Google Cloud ou nativo)
- [ ] Configurar permissões de microfone
- [ ] Implementar feedback visual do áudio

### FASE 4: Saída por Voz
- [ ] Integrar Text-to-Speech
- [ ] Configurar síntese de voz
- [ ] Adicionar controles de velocidade e pitch

### FASE 5: Sistema de Memória Local
- [ ] Setup de Room Database
- [ ] Criar modelos de dados
- [ ] Sincronização com backend

## Como Executar

### Pré-requisitos
- Android Studio Hedgehog ou superior
- SDK Android 24+
- JDK 11+

### Setup Inicial
1. Abrir o projeto em Android Studio
2. Sincronizar Gradle: `./gradlew syncDebug`
3. Executar: `./gradlew installDebug` ou usar o emulador do Android Studio

### Build
```bash
# Debug
./gradlew assembleDebug

# Release
./gradlew assembleRelease
```

## Dependências Principais
- Jetpack Compose
- Navigation Compose
- Room (Database)
- Retrofit + OkHttp (Networking)
- Hilt (Dependency Injection)
- Coroutines (Async)

## Próximos Passos
Criar os arquivos do projeto Android com estrutura base e build.gradle configurado.
