from agency_swarm import Agent
from agency_swarm.tools import BaseTool
import requests

class NarrationTool(BaseTool):
    """
    Tool to convert blog copy into AI-narrated audio using ElevenLabs.
    """
    async def run(self, text: str) -> str:
        # Call ElevenLabs API to generate narration
        response = requests.post("https://api.elevenlabs.io/narrate", json={"text": text})
        return response.json()

class NarrationAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Narration Agent",
            description="Converts blog copy into AI-narrated audio.",
            instructions="./instructions.md",  # instructions for the agent
            tools=[NarrationTool],
            temperature=0.5,
            max_prompt_tokens=25000,
        ) 