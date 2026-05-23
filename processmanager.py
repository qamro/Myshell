import subprocess

jobs = []

def run_process(cmd, background=False):
    if background:
        p = subprocess.Popen(cmd)
        jobs.append(p)
        print(f"[BG] PID: {p.pid}")
        return p
    else:
        return subprocess.run(cmd)