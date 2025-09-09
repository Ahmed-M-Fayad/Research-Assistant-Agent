"""
Intelligent Research Assistant - Application Entry Point
Flask application runner for development and production deployment
"""

import os
import sys
from app import create_app
from app.agents.research_agent import research_agent


def main():
    """Main application entry point"""
    try:
        # Create Flask application instance
        app = create_app()

        # Get configuration from environment
        host = os.getenv("FLASK_HOST", "127.0.0.1")
        port = int(os.getenv("FLASK_PORT", 5000))
        debug = os.getenv("FLASK_ENV", "development") == "development"

        print("🧠 Intelligent Research Assistant (3aref)")
        print("=" * 50)

        # Check agent health on startup
        print("🔍 Initializing Research Agent...")
        health = research_agent.health_check()
        if health["status"] == "healthy":
            print("✅ Research Agent is ready!")
            print("✅ Wikipedia tool initialized")
            print("✅ GROQ API connection verified")
        else:
            print(f"⚠️ Research Agent health check failed: {health['message']}")
            print("⚠️ Check your configs/.env file and GROQ_API_KEY")

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

        print("=" * 50)
        print("Press Ctrl+C to stop the server")
        print()

        # Start the Flask development server
        app.run(
            host=host,
            port=port,
            debug=debug,
            threaded=True,
            use_reloader=debug,  # Only auto-reload in debug mode
        )

    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        print(f"💡 Make sure your configs/.env file exists with GROQ_API_KEY")
        sys.exit(1)


if __name__ == "__main__":
    main()
