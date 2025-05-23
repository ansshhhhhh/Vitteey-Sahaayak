from langchain_tavily import TavilySearch
from langchain_community.agent_toolkits.polygon.toolkit import PolygonToolkit
from langchain_community.utilities.polygon import PolygonAPIWrapper
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from dotenv import load_dotenv
load_dotenv()

def add_polygon_tools(tools):
    """Add polygon tools to the list of tools."""
    polygon = PolygonAPIWrapper()
    toolkit = PolygonToolkit.from_polygon_api_wrapper(polygon)
    return toolkit.get_tools() + tools

def get_tools():
    """Get the tools for the agent."""
    yahooFinanceNewsTool = YahooFinanceNewsTool()
    tavilySearchTool = TavilySearch(max_results=3, topic="finance", character_limit=1000)
    wikipediaTool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(doc_content_chars_max=500))

    return add_polygon_tools([yahooFinanceNewsTool, tavilySearchTool, wikipediaTool])