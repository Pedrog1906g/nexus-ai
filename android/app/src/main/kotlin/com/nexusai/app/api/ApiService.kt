"""API Service"""
package com.nexusai.app.api

import com.google.gson.annotations.SerializedName
import retrofit2.http.*
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

// Data Classes
data class ChatRequest(
    val user_id: Int,
    val conversation_id: Int? = null,
    val message: String
)

data class ChatResponse(
    val conversation_id: Int,
    val user_message: MessageData,
    val ai_message: MessageData
)

data class MessageData(
    val id: Int,
    val sender: String,
    val content: String,
    val conversation_id: Int,
    val timestamp: String
)

data class UserRequest(
    val username: String,
    val email: String
)

data class UserResponse(
    val id: Int,
    val username: String,
    val email: String,
    val created_at: String,
    val updated_at: String
)

data class MemoryRequest(
    val category: String? = null,
    val key: String,
    val value: String
)

data class ConversationsResponse(
    val conversations: List<ConversationData>
)

data class ConversationData(
    val id: Int,
    val user_id: Int,
    val title: String?,
    val created_at: String,
    val updated_at: String
)

data class ConversationDetailResponse(
    val id: Int,
    val user_id: Int,
    val title: String?,
    val created_at: String,
    val updated_at: String,
    val messages: List<MessageData>
)

// API Interface
interface ApiService {
    @GET("/health")
    suspend fun getHealth(): HealthResponse
    
    @POST("/api/v1/chat")
    suspend fun sendMessage(@Body request: ChatRequest): ChatResponse
    
    @POST("/api/v1/users")
    suspend fun createUser(@Body request: UserRequest): UserResponse
    
    @GET("/api/v1/users/{user_id}")
    suspend fun getUser(@Path("user_id") userId: Int): UserResponse
    
    @POST("/api/v1/memory")
    suspend fun addMemory(
        @Query("user_id") userId: Int,
        @Body request: MemoryRequest
    ): MemoryData
    
    @GET("/api/v1/conversations/{user_id}")
    suspend fun getConversations(@Path("user_id") userId: Int): ConversationsResponse
    
    @GET("/api/v1/conversation/{conversation_id}")
    suspend fun getConversation(@Path("conversation_id") conversationId: Int): ConversationDetailResponse
}

data class HealthResponse(
    val status: String,
    val environment: String,
    val ai_provider: String
)

data class MemoryData(
    val id: Int,
    val user_id: Int,
    val category: String?,
    val key: String,
    val value: String,
    val created_at: String,
    val updated_at: String
)

// Retrofit Builder
object RetrofitClient {
    private const val BASE_URL = "http://10.0.2.2:8000/" // Para emulador Android
    
    val apiService: ApiService by lazy {
        Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
            .create(ApiService::class.java)
    }
    
    fun createWithUrl(baseUrl: String): ApiService {
        return Retrofit.Builder()
            .baseUrl(baseUrl)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
            .create(ApiService::class.java)
    }
}
