import importlib
from typing import Dict, List

from .plugin import Plugin
from .memory import JsonMemory

class PluginManager:
    """Loads and manages Machaa plugins."""

    def __init__(self, plugin_paths: List[str], memory: JsonMemory):
        self.plugin_paths = plugin_paths
        self.plugins: Dict[str, Plugin] = {}
        self.memory = memory

    def load_plugins(self):
        for path in self.plugin_paths:
            module = importlib.import_module(path)
            plugin_cls = getattr(module, 'Plugin', None)
            if plugin_cls is None:
                continue
            plugin_instance = plugin_cls()
            self.plugins[plugin_instance.name] = plugin_instance

    def execute(self, task: str) -> str:
        intent = self._extract_intent(task)
        if intent and intent in self.plugins:
            try:
                return self.plugins[intent].execute(task, self.memory)
            except NotImplementedError:
                pass

        for plugin in self.plugins.values():
            try:
                response = plugin.execute(task, self.memory)
                if response:
                    return response
            except NotImplementedError:
                continue
        return "No plugin could handle the task."

    def _extract_intent(self, task: str) -> str:
        task_lower = task.lower()
        for name, plugin in self.plugins.items():
            for kw in getattr(plugin, "intents", []):
                if task_lower.startswith(kw) or kw in task_lower:
                    return name
        return ""
