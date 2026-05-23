import os
from history import show_history
from aliases import set_alias

def handle_builtin(cmd):

    if cmd[0] == "cd":
        try:
            os.chdir(cmd[1])
        except:
            print("Invalid directory")
        return True

    if cmd[0] == "pwd":
        print(os.getcwd())
        return True

    if cmd[0] == "history":
        show_history()
        return True

    if cmd[0] == "alias":
        try:
            name = cmd[1]
            value = " ".join(cmd[2:])
            set_alias(name, value)
        except:
            print("Usage: alias ll ls -la")
        return True

    return False