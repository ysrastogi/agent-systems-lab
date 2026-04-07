import asyncio
import os
import json
from architectures.react.agent import ReactAgent
from core.runner import Runner

async def main():
    # Tools setup
    tools = [] # Placeholder for tool registration
    
    # Architecture: React
    react_agent = ReactAgent("React (v1)", tools)
    
    # Task: Research Assistant
    research_task_path = "tasks/research_assistant/task_definition.json"
    with open(research_task_path, "r") as f:
        research_task = json.load(f)
    
    # Runner for Research Assistant on React
    runner = Runner(react_agent, "research_assistant", "react")
    
    # Execute the run
    run_log = await runner.run(
        task_input=research_task["input"],
        expected_output=research_task["golden_output"]
    )
    
    # Repeat for other tasks if desired
    print(f"Full Run log saved to: {run_log['run_id']}")

if __name__ == "__main__":
    asyncio.run(main())
