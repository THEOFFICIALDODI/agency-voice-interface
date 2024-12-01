from agency_swarm import Agent
from agency_swarm.tools import BaseTool
import requests

class PerformanceAnalysisTool(BaseTool):
    """
    Tool to track podcast performance metrics.
    """
    async def run(self, podcast_id: str) -> dict:
        # Logic to analyze performance metrics
        response = requests.get(f"https://api.podtrac.com/{podcast_id}/analytics")
        return response.json()

class PerformanceAnalyzerAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Performance Analyzer Agent",
            description="Tracks download and listener metrics.",
            instructions="./instructions.md",  # instructions for the agent
            tools=[PerformanceAnalysisTool],
            temperature=0.5,
            max_prompt_tokens=25000,
        ) 