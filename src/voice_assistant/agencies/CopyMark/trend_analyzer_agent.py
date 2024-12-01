from agency_swarm import Agent
from agency_swarm.tools import BaseTool
import requests
# Ensure NLTK resources are downloaded
import nltk
nltk.download('punkt')

nltk.data.find('tokenizers/punkt')
from nltk import download

# Check if the 'punkt' tokenizer is already downloaded
if not nltk.data.find('tokenizers/punkt'):
    try:
        download('punkt')  # Download the tokenizer models if not already downloaded
    except Exception as e:
        print(f"Error downloading NLTK resources: {e}")

from pytrends.request import TrendReq  # Importing TrendReq after ensuring NLTK is set up
import os

class SearchWebTool(BaseTool):
    async def run(self, query: str) -> str:
        # Load the Tavily API key from environment variables
        api_key = os.getenv("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")  # Ensure this environment variable is set

        # Use Tavily API to search the web with the API key
        headers = {"Authorization": f"Bearer {api_key}"}  # Adjust based on API requirements
        response = requests.get(f"https://api.tavily.com/search?q={query}")
        return response.json()

class ExtractKeywordsTool(BaseTool):
    async def run(self, article: str) -> list:
        # Use NLTK to extract keywords
        tokens = nltk.word_tokenize(article)
        keywords = [word for word in tokens if word.isalnum()]
        return keywords

class AnalyzeKeywordsTool(BaseTool):
    async def run(self, keywords: list) -> dict:
        # Use Pytrends to analyze keywords
        pytrends = TrendReq()
        pytrends.build_payload(keywords, cat=0, timeframe='today 12-m', geo='', gprop='')
        return pytrends.interest_over_time()

class TrendAnalyzerAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Trend Analyzer Agent",
            description="Analyzes the latest AI trends and identifies content gaps.",
            instructions="./instructions.md",  # instructions for the agent
            tools=[SearchWebTool, ExtractKeywordsTool, AnalyzeKeywordsTool],
            temperature=0.5,
            max_prompt_tokens=25000,
        )