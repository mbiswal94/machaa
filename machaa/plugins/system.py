import subprocess
from ..plugin import Plugin

class Plugin(Plugin):
    name = "system"
    intents = ["run"]

    def execute(self, task: str, memory) -> str:
        cmd = task[4:] if task.lower().startswith("run ") else task
        try:
            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
            return output.strip()
        except subprocess.CalledProcessError as e:
            return f"Command failed: {e.output.strip()}"
