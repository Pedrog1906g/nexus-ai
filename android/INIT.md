# NEXUS AI - Android Project Structure

Este diretório conterá o aplicativo Android em Kotlin com Jetpack Compose.

## Estrutura será criada com:
- build.gradle.kts (build configuration)
- settings.gradle.kts (project settings)
- app/ (módulo principal da aplicação)
  - src/main/kotlin/com/nexusai/ (código-fonte)
  - src/main/res/ (recursos)
  - src/test/ (testes unitários)
  - src/androidTest/ (testes instrumentados)

## Como inicializar:

1. Abrir Android Studio
2. File > New > New Project
3. Selecionar "Empty Activity (Kotlin)"
4. Configure:
   - Name: NEXUS AI
   - Package name: com.nexusai.app
   - Save location: seu-caminho/android
   - Language: Kotlin
   - Minimum SDK: API 24
   - Build configuration language: Kotlin DSL

5. Ou usar template com Compose:
   - Selecionar "Compose Activity" em vez de "Empty Activity"

Após criação, a estrutura será iniciada.

## Tecnologias a serem adicionadas:
- Jetpack Compose
- Navigation Compose
- Room Database
- Retrofit
- Hilt DI
- Coroutines
