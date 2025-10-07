import wikipedia
from langchain_core.tools import tool
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Load environment configuration
config_path = "config/.env"
load_dotenv(config_path)

# Wikipedia Tool
class WikipediaInput(BaseModel):
    query: str = Field(description="The topic to search on Wikipedia")

class WikipediaOutput(BaseModel):
    result: str = Field(description="Wikipedia summary or error message")

@tool("Wikipedia", return_direct=True)
def wikipedia_tool(query: str) -> str:
    """
    Useful for when you need to look up information on Wikipedia.
    
    Args:
        query: The topic to search
        sentences: Number of summary sentences to return
    
    Returns:
        Wikipedia summary or error message
    """
    wikipedia.set_lang("en")
    
    try:
        return wikipedia.summary(query)

    except wikipedia.DisambiguationError as e:
        return f"⚠️ Multiple results found: {', '.join(e.options[:5])}..."
    
    except wikipedia.PageError:
        return "❌ No Wikipedia page found for this query."
    
    except Exception as e:
        return f"❌ Error fetching from Wikipedia: {str(e)}"
