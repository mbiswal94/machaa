# Machaa

Machaa is a local AI assistant framework designed to run on your Mac. The goal
is for Machaa to coordinate a collection of plug-in roles (developer, voice
interface, camera gesture detection, system command execution and more) while
keeping third-party API usage minimal. A simple JSON memory file stores history
and preferences so the assistant can learn over time.

## Features

- **Plugin architecture** – add new skills by dropping modules into
  `machaa/plugins` and listing them in `machaa/config.py`.
- **Third-party AI integration** – each plugin can decide which remote API to
  call and handle API limits.
- **OpenAI code generation** – the developer plugin uses the OpenAI API
  (if `OPENAI_API_KEY` is set) to generate or fix code snippets.
- **Voice and camera input** – capture speech and basic gestures
- **Voice commands** – use `python -m machaa.cli --voice` to speak a task and
  hear the summary spoken back
- **System and DevOps plugins** – run shell commands or simulate deployments
  with admin privileges when needed.
- **Intent-based dispatch** – Machaa extracts the user's intent before choosing
  which plugin should handle the task.
- **Local control** – run `python -m machaa.cli "your task"` to execute a task.

This repository currently includes example plugins for basic code generation,
voice input, and camera gesture recognition. Extend them or add new ones to suit
future roles such as data engineering or DevOps.

## Installation

Install the optional dependencies to enable voice features and OpenAI integration:

```bash
pip install -r requirements.txt
```


## Persistent memory

Machaa stores interaction history and preferences in `~/.machaa_memory.json`.
Plugins can read and update this file to learn your habits or track API usage.
