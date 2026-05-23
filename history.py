history = []

def add_history(command):
    history.append(command)

def show_history():
    for i, cmd in enumerate(history):
        print(f"{i + 1}: {cmd}")