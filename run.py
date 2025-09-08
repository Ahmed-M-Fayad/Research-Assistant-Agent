"""
Intelligent Research Assistant - Application Entry Point
Flask application runner for development and production deployment
"""

import os
import sys
from app import create_app


def main():
    """Main application entry point"""
    try:
        # Create Flask application instance
        app = create_app()

        # Get configuration from environment
        host = os.getenv("FLASK_HOST", "127.0.0.1")
        port = int(os.getenv("FLASK_PORT", 5000))
        debug = os.getenv("FLASK_ENV", "development") == "development"

        print("🧠 Intelligent Research Assistant")
        print("=" * 50)
        print(f"🌐 Server: http://{host}:{port}")
        print(f"🔧 Debug Mode: {debug}")
        print(f"📁 Environment: {os.getenv('FLASK_ENV', 'development')}")
        if debug:
            print("🔄 Auto-reload: Enabled")
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
        sys.exit(1)


if __name__ == "__main__":
    main()
