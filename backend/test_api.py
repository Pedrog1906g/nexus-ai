"""Test script for NEXUS AI API"""
import sys
import requests
import json
from time import sleep

BASE_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    print("\n📋 Testing Health Check...")
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        print(f"✅ Status: {response.status_code}")
        print(f"✅ Response: {response.json()}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_create_user():
    """Test user creation"""
    print("\n👤 Testing User Creation...")
    try:
        user_data = {
            "username": "pedro",
            "email": "pedro@example.com"
        }
        response = requests.post(
            f"{BASE_URL}/api/v1/users",
            json=user_data,
            timeout=5
        )
        print(f"✅ Status: {response.status_code}")
        result = response.json()
        print(f"✅ Response: {result}")
        return result.get("id")
    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def test_chat(user_id):
    """Test chat endpoint"""
    print(f"\n💬 Testing Chat (User ID: {user_id})...")
    try:
        chat_data = {
            "user_id": user_id,
            "message": "Olá Nexus, qual é o seu nome?"
        }
        response = requests.post(
            f"{BASE_URL}/api/v1/chat",
            json=chat_data,
            timeout=15
        )
        print(f"✅ Status: {response.status_code}")
        result = response.json()
        print(f"\n👤 User: {result['user_message']['content']}")
        print(f"🤖 Nexus: {result['ai_message']['content']}")
        return result.get("conversation_id")
    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def test_get_conversation(conversation_id):
    """Test get conversation"""
    print(f"\n📖 Testing Get Conversation (ID: {conversation_id})...")
    try:
        response = requests.get(
            f"{BASE_URL}/api/v1/conversation/{conversation_id}",
            timeout=5
        )
        print(f"✅ Status: {response.status_code}")
        result = response.json()
        print(f"✅ Messages: {len(result['messages'])} messages")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_add_memory(user_id):
    """Test adding memory"""
    print(f"\n🧠 Testing Add Memory (User ID: {user_id})...")
    try:
        memory_data = {
            "category": "personal_info",
            "key": "nome_favorito",
            "value": "Pedro"
        }
        response = requests.post(
            f"{BASE_URL}/api/v1/memory?user_id={user_id}",
            json=memory_data,
            timeout=5
        )
        print(f"✅ Status: {response.status_code}")
        print(f"✅ Response: {response.json()}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def main():
    """Run all tests"""
    print("🚀 NEXUS AI API Test Suite")
    print("=" * 50)
    
    # Test health
    if not test_health():
        print("\n❌ Server not responding. Make sure it's running!")
        sys.exit(1)
    
    sleep(1)
    
    # Test user creation
    user_id = test_create_user()
    if not user_id:
        print("\n❌ Failed to create user")
        sys.exit(1)
    
    sleep(1)
    
    # Test add memory
    test_add_memory(user_id)
    sleep(1)
    
    # Test chat
    conversation_id = test_chat(user_id)
    if not conversation_id:
        print("\n❌ Failed to chat")
        sys.exit(1)
    
    sleep(1)
    
    # Test get conversation
    test_get_conversation(conversation_id)
    
    print("\n" + "=" * 50)
    print("✅ All tests completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()
