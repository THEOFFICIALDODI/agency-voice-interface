from agency_swarm import Agent
from agency_swarm.tools import BaseTool

class PublishingTool(BaseTool):
    """
    Tool to publish the podcast episode to platforms.
    """
    async def run(self, podcast_file: str) -> str:
        # Logic to publish the podcast
        return "Publishing complete."

class PublishingAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Publishing Agent",
            description="Automates the uploading and distribution of the podcast episode.",
            instructions="./instructions.md",  # instructions for the agent
            tools=[PublishingTool],
            temperature=0.5,
            max_prompt_tokens=25000,
        ) 