from .plugin_manager import PluginManager
from .memory import JsonMemory

class Machaa:
    def __init__(self, plugins=None, memory_file="~/.machaa_memory.json"):
        self.memory = JsonMemory(memory_file)
        self.manager = PluginManager(plugins or [], self.memory)
        self.manager.load_plugins()

    def run_task(self, task: str) -> str:
        response = self.manager.execute(task)
        self.memory.append_interaction(task, response)
        return response

    def run_voice_command(self) -> str:
        """Capture a voice command, execute it, speak the result, and return it."""
        command = self.manager.execute("listen")
        if command.startswith("["):
            return command
        response = self.manager.execute(command)
        self.memory.append_interaction(command, response)
        self.manager.execute(f"speak {response}")
        return response
