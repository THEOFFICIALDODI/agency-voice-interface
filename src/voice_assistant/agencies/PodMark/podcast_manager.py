from agency_swarm import Agent

class PodcastManager(Agent):
    def __init__(self):
        super().__init__(
            name="Podcast Manager",
            description="Oversees the entire editing and conversion process of Twitch streams into podcasts.",
            instructions="./instructions.md",  # instructions for the agent
            tools=[],  # No specific tools for the Podcast Manager
            temperature=0.5,
            max_prompt_tokens=25000,
        ) 