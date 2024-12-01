from agency_swarm import Agent
from agency_swarm.tools import BaseTool

class AudioExtractionTool(BaseTool):
    """
    Tool to extract audio from Twitch stream video.
    """
    async def run(self, video_file: str) -> str:
        # Logic to extract audio from the video file
        return "Audio extraction complete."

class AudioExtractionAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Audio Extraction Agent",
            description="Extracts high-quality audio from the Twitch stream video.",
            instructions="./instructions.md",  # instructions for the agent
            tools=[AudioExtractionTool],
            temperature=0.5,
            max_prompt_tokens=25000,
        ) 