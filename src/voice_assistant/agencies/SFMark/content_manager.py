from agency_swarm import Agent
from agency_swarm.tools import BaseTool

class ContentManager(Agent):
    def __init__(self):
        super().__init__(
            name="Content Manager",
            description="Oversees the entire production process for short-form videos.",
            instructions="./instructions.md",  # instructions for the agent
            tools=[],  # No specific tools for the Content Manager
            temperature=0.5,
            max_prompt_tokens=25000,
        ) 