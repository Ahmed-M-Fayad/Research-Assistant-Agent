from langchain_core.tools import tool
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

# Load environment configuration
config_path = "config/.env"
load_dotenv(config_path)

# News Tool
class NewsInput(BaseModel):
    query: str = Field(description="The search query for news articles")
    max_results: int = Field(default=5, description="Maximum number of results to return")

class NewsOutput(BaseModel):
    result: List[Dict[str, Any]] = Field(description="List of news articles with source, title, and URL")

@tool("News Search", return_direct=True)
def news_tool(query: str, max_results: int = 5) -> List[Dict[str, Any]]:
    """
    Useful for when you need to find recent news articles on a topic.
    
    Args:
        query: The search query
        max_results: Maximum number of results to return
    
    Returns:
        Formatted list of article titles and URLs or error message
    """
    client = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))
    
    try:
        articles = client.get_everything(
            q=query, language="en", sort_by="relevancy"
        )
        if not articles["articles"]:
            return "❌ No articles found for this query."

        formatted_results = []
        for article in articles["articles"][:max_results]:
            formatted_results.append(
                {
                    "source": article["source"]["name"],
                    "title": article.get("title"),
                    "url": article.get("url"),
                }
            )

        return formatted_results

    except Exception as e:
        return f"❌ Error fetching from News API: {str(e)}"
