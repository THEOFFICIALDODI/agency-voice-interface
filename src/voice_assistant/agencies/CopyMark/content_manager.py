from agency_swarm import Agent
from agency_swarm.tools import BaseTool
import openai

class GenerateContentIdeasTool(BaseTool):
    """
    Tool to generate content ideas using OpenAI's chat completions API.
    """
    async def run(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use the latest model
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']

class ContentManager(Agent):
    def __init__(self):
        super().__init__(
            name="Content Manager",
            description="Responsible for generating content ideas and managing the content creation process.",
            instructions="./instructions.md",  # instructions for the agent
            tools=[GenerateContentIdeasTool],
            temperature=0.5,
            max_prompt_tokens=25000,
        )