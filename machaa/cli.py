import argparse

from .core import Machaa
from .config import DEFAULT_PLUGINS


def main():
    parser = argparse.ArgumentParser(description="Machaa assistant")
    parser.add_argument('task', nargs='?', help='Task description')
    parser.add_argument('-i', '--interactive', action='store_true', help='Run in interactive mode')
    parser.add_argument('-v', '--voice', action='store_true', help='Use voice input and output')
    args = parser.parse_args()

    assistant = Machaa(plugins=DEFAULT_PLUGINS)
    if args.voice:
        result = assistant.run_voice_command()
        print(result)
        return
    if args.interactive:
        while True:
            task = input('Machaa> ')
            if task.strip().lower() in {'exit', 'quit'}:
                break
            print(assistant.run_task(task))
    else:
        if not args.task:
            parser.error('task required unless --interactive is used')
        result = assistant.run_task(args.task)
        print(result)


if __name__ == '__main__':
    main()
