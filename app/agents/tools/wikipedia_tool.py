import wikipedia


class WikipediaTool:
    """Tool for fetching summaries from Wikipedia."""

    def __init__(self, language="en"):
        wikipedia.set_lang(language)

    def run(self, query: str, sentences: int = 3) -> str:
        """
        Search Wikipedia and return a short summary.

        Args:
            query (str): The topic to search.
            sentences (int): Number of summary sentences to return.

        Returns:
            str: Wikipedia summary or error message.
        """
        try:
            return wikipedia.summary(query, sentences=sentences)

        except wikipedia.DisambiguationError as e:
            return f"⚠️ Multiple results found: {', '.join(e.options[:5])}..."

        except wikipedia.PageError:
            return "❌ No Wikipedia page found for this query."

        except Exception as e:
            return f"❌ Error fetching from Wikipedia: {str(e)}"
