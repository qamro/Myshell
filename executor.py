import subprocess

def execute_command(cmd, background=False):

    try:
        if background:
            subprocess.Popen(cmd)
        else:
            subprocess.run(cmd)

    except FileNotFoundError:
        print(f"Command not found: {cmd[0]}")