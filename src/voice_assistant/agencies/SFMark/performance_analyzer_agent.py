from agency_swarm import Agent
from agency_swarm.tools import BaseTool
import requests

class PerformanceAnalysisTool(BaseTool):
    """
    Tool to track engagement metrics and provide actionable insights.
    """
    async def run(self, video_id: str) -> dict:
        # Logic to analyze performance metrics
        response = requests.get(f"https://api.bufferapp.com/1/videos/{video_id}/analytics")
        return response.json()

class PerformanceAnalyzerAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Performance Analyzer Agent",
            description="Tracks engagement metrics and provides actionable insights.",
            instructions="./instructions.md",  # instructions for the agent
            tools=[PerformanceAnalysisTool],
            temperature=0.5,
            max_prompt_tokens=25000,
        ) 