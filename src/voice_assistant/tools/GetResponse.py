import asyncio

from agency_swarm.agency import Agency
from agency_swarm.tools import BaseTool
from pydantic import Field, field_validator, model_validator

from voice_assistant.agencies import AGENCIES, AGENCIES_AND_AGENTS_STRING
from voice_assistant.utils.decorators import timeit_decorator


class GetResponse(BaseTool):
    """
    Checks the status of a task or retrieves the response from a specific agent within a specified agency.

    Use this tool after initiating a long-running task with 'SendMessageAsync'.
    Use the same parameters you used with 'SendMessageAsync' to check if the task is completed.
    If the task is completed, this tool will return the agent's response.
    If the task is still in progress, it will inform you accordingly.

    Available Agencies and Agents:
    {agency_agents}
    """

    agency_name: str = Field(..., description="The name of the agency.")
    agent_name: str | None = Field(
        None, description="The name of the agent, or None to use the default agent."
    )

    @field_validator("agency_name", mode="before")
    def check_agency_name(cls, value):
        if value not in AGENCIES:
            raise ValueError(
                f"Agency '{value}' not found. Available agencies: {', '.join(AGENCIES.keys())}"
            )
        return value

    @field_validator("agent_name", mode="before")
    def check_agent_name(cls, value):
        agencies = list(AGENCIES.values())
        agent_names = [agent.name for agency in agencies for agent in agency.agents]
        if value and value not in agent_names:
            raise ValueError(
                f"Agent '{value}' not found. Available agents: {', '.join(agent_names)}"
            )
        return value

    @model_validator(mode="after")
    def check_agency_in_async_mode(self):
        agency: Agency = AGENCIES.get(self.agency_name)
        if agency.async_mode != "threading":
            raise ValueError(
                f"Agency '{self.agency_name}' is not in threading mode. This tool is only available in threading mode."
            )
        return self

    @timeit_decorator
    async def run(self) -> str:
        agency: Agency = AGENCIES.get(self.agency_name)

        if self.agent_name is None or self.agent_name == agency.ceo.name:
            thread = agency.main_thread
        else:
            thread = agency.agents_and_threads.get(agency.ceo.name, {}).get(
                self.agent_name
            )

        if thread:
            return thread.check_status()
        else:
            return (
                f"No thread found between '{agency.ceo.name}' and '{self.agent_name}'"
            )


# Dynamically update the class docstring with the list of agencies and their agents
GetResponse.__doc__ = GetResponse.__doc__.format(
    agency_agents=AGENCIES_AND_AGENTS_STRING
)


if __name__ == "__main__":

    async def main():
        # Example usage for a specific thread
        tool = GetResponse(
            agency_name="ResearchAgency",
            agent_name="BrowsingAgent",
        )
        print(await tool.run())

    asyncio.run(main())
