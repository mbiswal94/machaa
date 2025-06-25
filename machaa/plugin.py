from typing import List


class Plugin:
    """Base class for Machaa plugins."""

    name = "base"
    intents: List[str] = []

    def __init__(self, config=None):
        self.config = config or {}

    def execute(self, task: str, memory) -> str:
        """Handle a task and return a response."""
        raise NotImplementedError
