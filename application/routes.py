"""
Flask routes for Research Agent integration
"""

from flask import render_template, request, flash, redirect, url_for
from application import app
from application.agents.research_agent import research_agent
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/")
@app.route("/home")
def home():
    """Home page"""
    return render_template("base.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        # Show search form
        return render_template("search.html")

    elif request.method == "POST":
        # Get query from form
        query = request.form.get("query", "")

        if not query:
            flash("Please enter a search query.", "warning")
            return redirect(url_for("search"))

        # Process with research agent
        result = research_agent.search(query)

        # Show results
        return render_template("search_results.html", query=query, result=result)


@app.route("/research")
def research():
    """New research page"""
    return render_template("research.html")


@app.route("/help")
def help():
    """Help page"""
    return render_template("help.html")


@app.route("/about")
def about():
    """About page"""
    return render_template("about.html")

@app.errorhandler(404)
def not_found(error):
    """404 error handler"""
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    """500 error handler"""
    logger.error(f"Internal error: {str(error)}")
    return render_template("500.html"), 500
