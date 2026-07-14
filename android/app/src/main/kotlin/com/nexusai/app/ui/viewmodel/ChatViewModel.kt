"""Chat ViewModel"""
package com.nexusai.app.ui.viewmodel

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.nexusai.app.api.*
import com.nexusai.app.data.repository.ChatRepository
import com.nexusai.app.data.repository.UserRepository
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

data class ChatMessage(
    val id: Int,
    val sender: String,
    val content: String,
    val timestamp: String
)

data class ChatUiState(
    val messages: List<ChatMessage> = emptyList(),
    val isLoading: Boolean = false,
    val error: String? = null,
    val currentConversationId: Int? = null,
    val userId: Int? = null,
    val username: String? = null
)

class ChatViewModel : ViewModel() {
    
    private val apiService = RetrofitClient.apiService
    private val chatRepository = ChatRepository(apiService)
    private val userRepository = UserRepository(apiService)
    
    private val _uiState = MutableStateFlow(ChatUiState())
    val uiState: StateFlow<ChatUiState> = _uiState.asStateFlow()
    
    fun initializeUser(username: String, email: String) {
        viewModelScope.launch {
            try {
                _uiState.update { it.copy(isLoading = true, error = null) }
                val user = userRepository.createUser(username, email)
                _uiState.update { 
                    it.copy(
                        isLoading = false,
                        userId = user.id,
                        username = user.username
                    )
                }
                loadConversations(user.id)
            } catch (e: Exception) {
                _uiState.update { 
                    it.copy(
                        isLoading = false,
                        error = "Erro ao criar usuário: ${e.message}"
                    )
                }
            }
        }
    }
    
    fun sendMessage(message: String) {
        val userId = _uiState.value.userId ?: return
        
        if (message.isBlank()) return
        
        viewModelScope.launch {
            try {
                _uiState.update { it.copy(isLoading = true, error = null) }
                
                // Add user message immediately
                val userMsg = ChatMessage(
                    id = 0,
                    sender = "user",
                    content = message,
                    timestamp = System.currentTimeMillis().toString()
                )
                
                _uiState.update { 
                    it.copy(
                        messages = it.messages + userMsg
                    )
                }
                
                // Send to API
                val response = chatRepository.sendMessage(
                    userId = userId,
                    conversationId = _uiState.value.currentConversationId,
                    message = message
                )
                
                // Add AI response
                val aiMsg = ChatMessage(
                    id = response.ai_message.id,
                    sender = response.ai_message.sender,
                    content = response.ai_message.content,
                    timestamp = response.ai_message.timestamp
                )
                
                _uiState.update { 
                    it.copy(
                        messages = it.messages + aiMsg,
                        isLoading = false,
                        currentConversationId = response.conversation_id
                    )
                }
            } catch (e: Exception) {
                _uiState.update { 
                    it.copy(
                        isLoading = false,
                        error = "Erro ao enviar mensagem: ${e.message}"
                    )
                }
            }
        }
    }
    
    private fun loadConversations(userId: Int) {
        viewModelScope.launch {
            try {
                val conversations = chatRepository.getConversations(userId)
                if (conversations.conversations.isNotEmpty()) {
                    val lastConversation = conversations.conversations.first()
                    loadConversationMessages(lastConversation.id)
                }
            } catch (e: Exception) {
                // Fail silently, it's okay if there are no conversations yet
            }
        }
    }
    
    private fun loadConversationMessages(conversationId: Int) {
        viewModelScope.launch {
            try {
                val conversation = chatRepository.getConversation(conversationId)
                val messages = conversation.messages.map { msg ->
                    ChatMessage(
                        id = msg.id,
                        sender = msg.sender,
                        content = msg.content,
                        timestamp = msg.timestamp
                    )
                }
                
                _uiState.update { 
                    it.copy(
                        messages = messages,
                        currentConversationId = conversationId
                    )
                }
            } catch (e: Exception) {
                // Fail silently
            }
        }
    }
    
    fun clearError() {
        _uiState.update { it.copy(error = null) }
    }
}
