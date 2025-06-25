import json
from pathlib import Path
from typing import Any, Dict, List

class JsonMemory:
    """Simple JSON-based persistent memory for Machaa."""

    def __init__(self, path: str):
        self.path = Path(path).expanduser()
        if not self.path.exists():
            self.data: Dict[str, Any] = {"history": [], "prefs": {}}
            self._write()
        else:
            self._read()

    def _read(self):
        try:
            with self.path.open("r") as f:
                self.data = json.load(f)
        except Exception:
            self.data = {"history": [], "prefs": {}}

    def _write(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w") as f:
            json.dump(self.data, f, indent=2)

    def append_interaction(self, task: str, response: str):
        self.data.setdefault("history", []).append({"task": task, "response": response})
        self._write()

    def get_pref(self, key: str, default: Any = None) -> Any:
        return self.data.get("prefs", {}).get(key, default)

    def set_pref(self, key: str, value: Any):
        self.data.setdefault("prefs", {})[key] = value
        self._write()
