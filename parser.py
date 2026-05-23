import shlex

def parse_command(command):
    return shlex.split(command)