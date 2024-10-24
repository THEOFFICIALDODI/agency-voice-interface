import asyncio

from agency_swarm.tools import BaseTool
from pydantic import Field, field_validator


class GetResponse(BaseTool):
    """
    This tool allows you to check the status of a task or get a response from a specified recipient agent, if the task has been completed. You must always use the 'SendMessage' tool with the designated agent first.
    """

    recipient: str = Field(
        ...,
        description="Recipient agent that you want to check the status of.",
    )

    async def run(self) -> str:
        # Assuming that agents_and_threads is part of the shared state
        agents_and_threads = self._shared_state.get("agents_and_threads", {})
        caller_agent_name = self._shared_state.get("caller_agent_name")

        if not caller_agent_name:
            return "Caller agent name is not available in the shared state."

        thread = agents_and_threads.get(self.recipient, {}).get(caller_agent_name)

        if thread:
            status = await thread.check_status()
            return status
        else:
            return f"No active thread found for recipient '{self.recipient}'."


if __name__ == "__main__":

    async def main():
        tool = GetResponse(recipient="AgentA")
        print(await tool.run())

    asyncio.run(main())
