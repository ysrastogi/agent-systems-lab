from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

class Agent(ABC):
    """Base class for all agent architectures."""
    
    def __init__(self, name: str, tools: List[Any]):
        self.name = name
        self.tools = tools

    @abstractmethod
    async def run(self, task_input: str) -> Dict[str, Any]:
        """Runs the agent on the given task and returns a summary of execution."""
        pass
