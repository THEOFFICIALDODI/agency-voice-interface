from agency_swarm import Agent
from agency_swarm.tools import BaseTool

class AudioEditingTool(BaseTool):
    """
    Tool to clean and edit the audio.
    """
    async def run(self, audio_file: str) -> str:
        # Logic to edit the audio
        return "Audio editing complete."

class AudioEditingAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Audio Editing Agent",
            description="Cleans and edits the audio for clarity.",
            instructions="./instructions.md",  # instructions for the agent
            tools=[AudioEditingTool],
            temperature=0.5,
            max_prompt_tokens=25000,
        ) 