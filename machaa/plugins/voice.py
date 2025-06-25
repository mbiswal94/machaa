from ..plugin import Plugin

try:  # pragma: no cover - optional dependency
    import speech_recognition as sr
except ImportError:  # pragma: no cover - optional dependency
    sr = None

try:  # pragma: no cover - optional dependency
    import pyttsx3
except ImportError:  # pragma: no cover - optional dependency
    pyttsx3 = None

class Plugin(Plugin):
    name = "voice"
    intents = ["listen", "speak"]

    def _listen(self) -> str:
        if sr is None:
            return "[speech_recognition not installed]"
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                audio = recognizer.listen(source, timeout=5)
                return recognizer.recognize_google(audio)
            except Exception:
                return "[could not understand audio]"

    def _speak(self, text: str) -> str:
        if pyttsx3 is None:
            return "[pyttsx3 not installed]"
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        return "[spoken]"

    def execute(self, task: str, memory) -> str:
        task_lower = task.lower()
        if task_lower.startswith("listen"):
            return self._listen()
        if task_lower.startswith("speak"):
            text = task[len("speak"):].strip()
            return self._speak(text)
        return ""
