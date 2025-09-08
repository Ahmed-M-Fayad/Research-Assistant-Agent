"""
Intelligent Research Assistant - Flask Application Factory
Main application configuration and initialization
"""

from flask import Flask, render_template


def create_app():
    """Simple app for local development"""

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "local-dev-key"
    app.config["DEBUG"] = True

    # Simple routes
    @app.route("/")
    def home():
        return render_template("base.html")
    
    @app.route("/about")
    def about():
        return render_template("about.html")
    
    @app.route("/help")
    def help():
        return render_template("help.html")
    
    @app.route("/research")
    def research():
        return render_template("research.html")

    @app.route("/index")
    def index():
        return render_template("index.html")
    
    return app
