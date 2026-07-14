#!/bin/bash
# Quick start script for NEXUS AI

echo "🚀 NEXUS AI - Quick Start"
echo "=========================="
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if backend is already running
check_backend() {
    if curl -s http://localhost:8000/health > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Backend already running${NC}"
        return 0
    fi
    return 1
}

# Start Backend
start_backend() {
    echo -e "${BLUE}📦 Starting Backend...${NC}"
    cd backend
    
    if [ ! -d "venv" ]; then
        echo -e "${YELLOW}Creating virtual environment...${NC}"
        python3 -m venv venv
    fi
    
    source venv/bin/activate 2>/dev/null || . venv/Scripts/activate 2>/dev/null
    
    if ! python -c "import fastapi" 2>/dev/null; then
        echo -e "${YELLOW}Installing dependencies...${NC}"
        pip install -q -r requirements.txt
    fi
    
    # Remove old database for fresh start
    rm -f nexus_ai.db
    
    echo -e "${GREEN}✅ Backend ready!${NC}"
    echo -e "${YELLOW}Starting Uvicorn...${NC}"
    uvicorn app.main:app --reload --port 8000
}

# Display Android instructions
show_android_instructions() {
    echo -e "${BLUE}📱 Android App${NC}"
    echo "=============="
    echo ""
    echo -e "${YELLOW}Option 1: Android Studio (Recommended)${NC}"
    echo "  1. File > Open > nexus-ai/android"
    echo "  2. Wait for Gradle sync"
    echo "  3. Run > Run 'app'"
    echo ""
    echo -e "${YELLOW}Option 2: Command Line${NC}"
    echo "  cd android"
    echo "  ./gradlew assembleDebug"
    echo "  ./gradlew installDebug"
    echo ""
}

# Test API
test_api() {
    echo ""
    echo -e "${BLUE}🧪 Testing API...${NC}"
    sleep 2
    
    cd backend
    source venv/bin/activate 2>/dev/null || . venv/Scripts/activate 2>/dev/null
    python test_api.py
}

# Main menu
main() {
    if check_backend; then
        echo -e "${GREEN}Backend is running!${NC}"
        echo ""
        echo "Choose action:"
        echo "1) Test API"
        echo "2) Show Android setup"
        echo "3) Exit"
        read -p "Enter choice: " choice
        
        case $choice in
            1) test_api ;;
            2) show_android_instructions ;;
            3) exit 0 ;;
            *) echo "Invalid choice" ;;
        esac
    else
        echo -e "${YELLOW}Backend not running. Starting...${NC}"
        start_backend
    fi
}

main
