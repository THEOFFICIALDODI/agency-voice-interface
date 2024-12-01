from agency_swarm import Agent
from agency_swarm.tools import BaseTool
import requests

class VisualGenerationTool(BaseTool):
    """
    Tool to identify or generate video clips/images using Runway or Pexels API.
    """
    async def run(self, keywords: str) -> list:
        # Call Pexels API to search for visuals
        response = requests.get(f"https://api.pexels.com/v1/search?query={keywords}", headers={"Authorization": "YOUR_API_KEY"})
        return response.json()

class VisualGeneratorAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Visual Generator Agent",
            description="Identifies or generates video clips/images in sync with the narration.",
            instructions="./instructions.md",  # instructions for the agent
            tools=[VisualGenerationTool],
            temperature=0.5,
            max_prompt_tokens=25000,
        ) 