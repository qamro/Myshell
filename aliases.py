aliases = {}

def set_alias(name, value):
    aliases[name] = value

def resolve_alias(cmd):
    if cmd[0] in aliases:
        return aliases[cmd[0]].split() + cmd[1:]
    return cmd