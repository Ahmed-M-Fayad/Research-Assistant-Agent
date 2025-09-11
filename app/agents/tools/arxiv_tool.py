from langchain_core.tools import tool
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from dotenv import load_dotenv
import arxiv

# Load environment configuration
config_path = "config/.env"
load_dotenv(config_path)

# ArXiv Tool
class ArxivInput(BaseModel):
    query: str = Field(description="The search query for academic papers")
    max_results: int = Field(default=5, description="Maximum number of results to return")

class ArxivOutput(BaseModel):
    result: List[Dict[str, Any]] = Field(description="List of papers with title, summary, and PDF URL")

@tool("ArXiv Papers", args_schema=ArxivInput, return_direct=True)
def arxiv_tool(query: str, max_results: int = 5) -> List[Dict[str, Any]]:
    """
    Useful for when you need to find academic papers on a specific topic.
    
    Args:
        query: The search query
        max_results: Maximum number of results to return
    
    Returns:
        Formatted list of paper titles and summaries or error message
    """
    try:
        # Construct the default API client.
        client = arxiv.Client()

        # Search for the most relevant articles matching the query.
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.Relevance,
        )

        results = list(client.results(search))

        if not results:
            return "❌ No papers found for this query."

        formatted_results = []
        for result in results:
            formatted_results.append(
                {
                    "title": result.title,
                    "summary": result.summary,
                    "paper url": result.pdf_url,
                }
            )

        return formatted_results

    except Exception as e:
        return f"❌ Error fetching from arXiv: {str(e)}"