import json
import os
import time
from datetime import datetime
from typing import Dict, Any, List, Optional
from core.agent_base import Agent

class Runner:
    """Class to manage and log agent runs."""
    
    def __init__(self, agent: Agent, task_name: str, architecture_name: str):
        self.agent = agent
        self.task_name = task_name
        self.architecture_name = architecture_name
        self.base_dir = f"runs/{task_name}/{architecture_name}"
        os.makedirs(self.base_dir, exist_ok=True)
        self.run_id = self._get_next_run_id()

    def _get_next_run_id(self) -> str:
        """Determines the next sequential run ID (run_001.json)."""
        existing_runs = [
            f for f in os.listdir(self.base_dir) if f.startswith("run_") and f.endswith(".json")
        ]
        if not existing_runs:
            return "run_001.json"
        
        last_id = max([int(f.split("_")[1].split(".")[0]) for f in existing_runs])
        return f"run_{last_id + 1:03d}.json"

    async def run(self, task_input: str, expected_output: Optional[Any] = None) -> Dict[str, Any]:
        """Runs the agent and logs performance metrics."""
        start_time = time.time()
        
        print(f"Starting run {self.run_id} for task: {self.task_name} using arch: {self.architecture_name}")
        
        try:
            result = await self.agent.run(task_input)
            latency = time.time() - start_time
            
            log_data = {
                "run_id": self.run_id,
                "timestamp": datetime.now().isoformat(),
                "task": self.task_name,
                "architecture": self.architecture_name,
                "input": task_input,
                "expected": expected_output,
                "result": result,
                "metrics": {
                    "latency": round(latency, 2),
                    "token_usage": result.get("token_usage", 0),
                    "success": self._evaluate_success(result.get("response"), expected_output)
                },
                "steps": result.get("steps", [])
            }
            
            with open(os.path.join(self.base_dir, self.run_id), "w") as f:
                json.dump(log_data, f, indent=4)
            
            print(f"Run completed successfully. Logs saved to {self.base_dir}/{self.run_id}")
            return log_data
            
        except Exception as e:
            error_data = {
                "run_id": self.run_id,
                "timestamp": datetime.now().isoformat(),
                "error": str(e),
                "metrics": {"success": False}
            }
            with open(os.path.join(self.base_dir, self.run_id), "w") as f:
                json.dump(error_data, f, indent=4)
            raise e

    def _evaluate_success(self, actual: Any, expected: Any) -> bool:
        """Stub for success evaluation."""
        if expected is None: return True
        return actual == expected
