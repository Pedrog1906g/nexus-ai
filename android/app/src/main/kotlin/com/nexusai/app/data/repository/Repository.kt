"""Repository Pattern"""
package com.nexusai.app.data.repository

import com.nexusai.app.api.*

class ChatRepository(private val apiService: ApiService) {
    
    suspend fun sendMessage(userId: Int, conversationId: Int?, message: String): ChatResponse {
        return apiService.sendMessage(
            ChatRequest(
                user_id = userId,
                conversation_id = conversationId,
                message = message
            )
        )
    }
    
    suspend fun getConversations(userId: Int): ConversationsResponse {
        return apiService.getConversations(userId)
    }
    
    suspend fun getConversation(conversationId: Int): ConversationDetailResponse {
        return apiService.getConversation(conversationId)
    }
}

class UserRepository(private val apiService: ApiService) {
    
    suspend fun createUser(username: String, email: String): UserResponse {
        return apiService.createUser(
            UserRequest(username = username, email = email)
        )
    }
    
    suspend fun getUser(userId: Int): UserResponse {
        return apiService.getUser(userId)
    }
}

class MemoryRepository(private val apiService: ApiService) {
    
    suspend fun addMemory(userId: Int, category: String?, key: String, value: String): MemoryData {
        return apiService.addMemory(
            userId,
            MemoryRequest(category = category, key = key, value = value)
        )
    }
}
