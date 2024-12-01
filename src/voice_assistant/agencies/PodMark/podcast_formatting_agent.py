from agency_swarm import Agent
from agency_swarm.tools import BaseTool

class PodcastFormattingTool(BaseTool):
    """
    Tool to format the audio to fit podcast standards.
    """
    async def run(self, audio_file: str) -> str:
        # Logic to format the audio
        return "Podcast formatting complete."

class PodcastFormattingAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Podcast Formatting Agent",
            description="Formats the audio to fit podcast standards.",
            instructions="./instructions.md",  # instructions for the agent
            tools=[PodcastFormattingTool],
            temperature=0.5,
            max_prompt_tokens=25000,
        ) 