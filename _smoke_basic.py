"""Temporary smoke test for the basic (no-MCP) hosted agent.

Confirms hosted Agent Framework agents run on the new public Foundry
account via the Responses protocol. Safe to delete.
"""

from __future__ import annotations

import asyncio
import os

from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient


async def _main() -> None:
    endpoint = os.environ["AZURE_AI_PROJECT_ENDPOINT"]
    agent_name = "agent-framework-agent-basic-responses"
    prompt = "Hi! In one sentence, what can you help me with?"
    async with DefaultAzureCredential() as credential:
        async with AIProjectClient(endpoint, credential, allow_preview=True) as client:
            openai_client = client.get_openai_client(agent_name=agent_name)
            response = await openai_client.responses.create(
                model=agent_name,
                input=prompt,
            )
            print("=== output_text ===")
            print(getattr(response, "output_text", response))


if __name__ == "__main__":
    asyncio.run(_main())
