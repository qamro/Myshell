import subprocess

def execute_pipeline(commands):
    processes = []
    prev = None

    for cmd in commands:
        if prev is None:
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        else:
            p = subprocess.Popen(
                cmd,
                stdin=prev.stdout,
                stdout=subprocess.PIPE
            )

        processes.append(p)
        prev = p

    output, _ = processes[-1].communicate()
    print(output.decode())