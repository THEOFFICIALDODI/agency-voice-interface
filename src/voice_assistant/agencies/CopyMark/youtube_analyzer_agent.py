from agency_swarm import Agent
from agency_swarm.tools import BaseTool
import requests

class AnalyzeChannelPerformanceTool(BaseTool):
    async def run(self, channel_id: str) -> dict:
        # Analyze channel performance using YouTube API
        response = requests.get(f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key=YOUR_API_KEY")
        return response.json()

class YouTubeAnalyzerAgent(Agent):
    def __init__(self):
        super().__init__(
            name="YouTube Analyzer Agent",
            description="Identifies content gaps on YouTube and analyzes channel performance.",
            instructions="./instructions.md",  # instructions for the agent
            tools=[AnalyzeChannelPerformanceTool],
            temperature=0.5,
            max_prompt_tokens=25000,
        )