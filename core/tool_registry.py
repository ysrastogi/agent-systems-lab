from typing import Dict, Any, Callable, List
import inspect

class ToolRegistry:
    """Registry for agent tools."""
    
    def __init__(self):
        self.tools: Dict[str, Dict[str, Any]] = {}

    def register(self, func: Callable):
        """Register a tool with its documentation and parameters."""
        name = func.__name__
        doc = func.__doc__
        params = inspect.signature(func).parameters
        
        self.tools[name] = {
            "name": name,
            "description": doc,
            "parameters": {
                p_name: {
                    "type": str(p_type.annotation),
                    "default": p_type.default if p_type.default is not inspect.Parameter.empty else None
                }
                for p_name, p_type in params.items()
            },
            "func": func
        }
        return func

    def list_tools(self) -> List[Dict[str, Any]]:
        """Lists all registered tools."""
        return [
            {k: v for k, v in tool.items() if k != "func"} 
            for tool in self.tools.values()
        ]

    def call(self, name: str, **kwargs) -> Any:
        """Call a registered tool by name with arguments."""
        if name not in self.tools:
            raise ValueError(f"Tool {name} not found.")
        return self.tools[name]["func"](**kwargs)
