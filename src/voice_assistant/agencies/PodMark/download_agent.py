from agency_swarm import Agent
from agency_swarm.tools import BaseTool
import requests

class DownloadTool(BaseTool):
    """
    Tool to download Twitch stream videos.
    """
    async def run(self, stream_url: str) -> str:
        # Logic to download the Twitch stream
        response = requests.get(stream_url)
        # Save the video file locally
        with open("downloaded_stream.mp4", "wb") as f:
            f.write(response.content)
        return "Download complete."

class DownloadAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Download Agent",
            description="Handles downloading the Twitch stream files.",
            instructions="./instructions.md",  # instructions for the agent
            tools=[DownloadTool],
            temperature=0.5,
            max_prompt_tokens=25000,
        ) 