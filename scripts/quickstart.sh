#!/bin/bash
# Smart AI Router Quick Start Script

echo "🚀 Smart AI Router Setup"
echo "==============================="

# Check API key
if [ -z "$OPENROUTER_API_KEY" ]; then
    echo "⚠️  OPENROUTER_API_KEY not set"
    echo "Get your key from: https://openrouter.ai/keys"
    echo ""
    echo "Set it with:"
    echo "  export OPENROUTER_API_KEY=your-key-here"
    echo ""
    echo "Or create a .env file in the project root"
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt --quiet

# Test connection
echo "🔌 Testing OpenRouter connection..."
python3 << EOF
from openai import OpenAI
import os

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

try:
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[{"role": "user", "content": "Hello!"}],
        max_tokens=50
    )
    print("✅ Connection successful!")
    print(f"   Model used: {response.model}")
except Exception as e:
    print(f"❌ Connection failed: {e}")
EOF

# Check credits
echo ""
echo "💰 Checking OpenRouter credits..."
echo "   Visit: https://openrouter.ai/account"
echo ""
echo "💡 Tip: Buy \$10 in credits to unlock 1000 free requests/day"
echo ""

# Display dashboard if available
if [ -f "scripts/dashboard.py" ]; then
    echo "📊 Current Usage:"
    python3 scripts/dashboard.py
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Review the README.md for usage examples"
echo "  2. Try the examples in examples/"
echo "  3. Run tests with: pytest tests/"
echo ""
echo "Quick example:"
echo "  from smart_router import SmartRouter"
echo "  router = SmartRouter(preset='creative-ideation')"
echo "  response = router.chat.completions.create(messages=[...])"
