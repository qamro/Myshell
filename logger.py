from datetime import datetime

LOG_FILE = "myshell.log"

def log_command(command):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {command}\n")