"""
Intelligent Research Assistant - Application Entry Point
Flask application runner for development and production deployment
"""

import os
import sys
from dotenv import load_dotenv  # Load environment variables and configurations
from application import app  # Import the Flask app instance

try:
    dotenv_path = "configs/.env"
    load_dotenv(dotenv_path)  # Load environment variables from .env file
except Exception as e:
    print(f"❌ Error loading .env file: {e}")
    sys.exit(1)


try:
    # Get configuration from environment
    host = os.getenv("FLASK_HOST", "127.0.0.1")
    port = int(os.getenv("FLASK_PORT", 5000))
    debug = os.getenv("FLASK_ENV", "development") == "development"

    print("🧠 Intelligent Research Assistant (3aref)")
    print("=" * 50)

    # Check agent health on startup
    print("🔍 Initializing Research Agent...")
    print(f"\n🌐 Server: http://{host}:{port}")
    print(f"🔧 Debug Mode: {debug}")
    print(f"📁 Environment: {os.getenv('FLASK_ENV', 'development')}")
    if debug:
        print("🔄 Auto-reload: Enabled")

    print("\n📖 Available routes:")
    print("   • /           - Home page")
    print("   • /search     - Search interface")
    print("   • /research   - New research")
    print("   • /help       - Help page")
    print("   • /about      - About page")
    print("   • /health     - Health check")
    print("   • /api/search - API endpoint")

    print("\n🚀 Starting application...")
    app.run(
        host=os.getenv("FLASK_HOST", "127.0.0.1"),
        port=os.getenv("FLASK_PORT", 5000),
        debug=os.getenv("FLASK_DEBUG", False),
        threaded=True,
        use_reloader=os.getenv("FLASK_DEBUG", False),  # Only auto-reload in debug mode
    )

    print("=" * 50)
    print("Press Ctrl+C to stop the server")
    print()

except KeyboardInterrupt:
    print("\n👋 Server stopped by user")
    sys.exit(0)
except Exception as e:
    print(f"❌ Error starting application: {e}")
    print(f"💡 Make sure your configs/.env file exists with GROQ_API_KEY")
    sys.exit(1)
