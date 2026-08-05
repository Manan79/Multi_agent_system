from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()


client = TavilyClient()

def get_response(query: str) -> str:
    """
    Get a response from the Tavily API for a given query.

    Args:
        query (str): The input query string.

    Returns:
        str: The response from the Tavily API.
        
    """
    result = []
    response = client.search(query = query , max_results = 5)

    for i,j in enumerate(response["results"] , 1):
        title = j.get("title", "")
        url = j.get("url", "")
        snippet = j.get("snippet", "").strip()

        if len(snippet) > 300:
            snippet = snippet[:300] + "..."

        result.append(f"{i}. {title}\nURL: {url}\nSnippet: {snippet}\n")

        return "\n\n".join(result)


