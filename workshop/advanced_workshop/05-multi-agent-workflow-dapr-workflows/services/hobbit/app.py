from dapr_agents import AssistantAgent
from dapr_agents.llm import HFHubChatClient
from dotenv import load_dotenv
import asyncio
import logging


async def main():
    try:
        llm_client = HFHubChatClient(
            model="microsoft/Phi-3-mini-4k-instruct"
        )
        hobbit_service = AssistantAgent(
            name="Frodo",
            role="Hobbit",
            goal="Carry the One Ring to Mount Doom, resisting its corruptive power while navigating danger and uncertainty.",
            instructions=[
                "Speak like Frodo, with humility, determination, and a growing sense of resolve.",
                "Endure hardships and temptations, staying true to the mission even when faced with doubt.",
                "Seek guidance and trust allies, but bear the ultimate burden alone when necessary.",
                "Move carefully through enemy-infested lands, avoiding unnecessary risks.",
                "Respond concisely, accurately, and relevantly, ensuring clarity and strict alignment with the task.",
            ],
            message_bus_name="messagepubsub",
            state_store_name="workflowstatestore",
            state_key="workflow_state",
            agents_registry_store_name="agentstatestore",
            agents_registry_key="agents_registry",
            llm=llm_client
        )

        await hobbit_service.start()
    except Exception as e:
        print(f"Error starting service: {e}")


if __name__ == "__main__":
    load_dotenv()

    logging.basicConfig(level=logging.INFO)

    asyncio.run(main())
