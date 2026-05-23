import signal
import sys

def handle_sigint(signum, frame):
    print("\n[myshell] Ctrl+C caught (use 'exit' to quit)")

signal.signal(signal.SIGINT, handle_sigint)