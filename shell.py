import os

from parser import parse_command
from shellbuiltins import handle_builtin
from processmanager import run_process
from pipeline import execute_pipeline

from history import add_history
from aliases import resolve_alias
from logger import log_command

def run_shell():

    while True:
        try:
            cwd = os.getcwd()
            cmd_input = input(f"myshell:{cwd}$ ")

            if not cmd_input.strip():
                continue

            # log + history
            add_history(cmd_input)
            log_command(cmd_input)

            # EXIT
            if cmd_input.strip() == "exit":
                print("Bye 👋")
                break

            # MULTI COMMANDS (&&)
            commands = cmd_input.split("&&")

            for command in commands:

                command = command.strip()

                # BACKGROUND CHECK
                background = False
                if command.endswith("&"):
                    background = True
                    command = command[:-1].strip()

                # PIPE SUPPORT
                if "|" in command:
                    parts = command.split("|")
                    pipeline_cmds = [
                        parse_command(p.strip())
                        for p in parts
                    ]
                    execute_pipeline(pipeline_cmds)
                    continue

                # PARSE
                cmd = parse_command(command)

                # ALIASES
                cmd = resolve_alias(cmd)

                if not cmd:
                    continue

                # BUILTINS
                if handle_builtin(cmd):
                    continue

                # EXECUTE
                run_process(cmd, background)

        except KeyboardInterrupt:
            print()
        except Exception as e:
            print(f"Error: {e}")