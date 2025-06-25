import os
from ..plugin import Plugin

try:
    import openai
except ImportError:  # pragma: no cover - optional dependency
    openai = None

API_LIMIT = 3

class Plugin(Plugin):
    name = "developer"
    intents = ["code", "fix", "write", "generate"]

    def _generate_with_openai(self, prompt: str) -> str:
        """Call OpenAI API to generate or fix code."""
        if openai is None:
            return "openai package not installed"
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return "OpenAI API key not configured"
        openai.api_key = api_key
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
            )
            return completion.choices[0].message["content"].strip()
        except Exception as e:
            return f"OpenAI API error: {e}"

    def execute(self, task: str, memory) -> str:
        usage = memory.get_pref("dev_api_usage", 0)
        if usage >= API_LIMIT:
            return "Developer API limit reached"
        memory.set_pref("dev_api_usage", usage + 1)
        return self._generate_with_openai(task)
