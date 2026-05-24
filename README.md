# 🐚 MyShell — Mini Unix-like Shell 
> A lightweight, modular, Unix-like shell built from scratch in Python, simulating real operating system behavior such as process management, piping, job execution, and command parsing.

---

## 🚀 Overview

**MyShell** is a systems-level project that replicates core features of a Unix shell such as `bash`.  
It is designed to help understand how operating systems handle:

- Processes
- Pipes (IPC)
- Command execution
- Background jobs
- Shell architecture

This project evolves step-by-step from a basic command executor to a fully modular mini-shell.

---

## 📸 Demo Screenshots

### 🔹 Basic Commands


<img width="1620" height="1080" alt="Myshell" src="https://github.com/user-attachments/assets/d336b50a-1e56-47aa-bfcf-de595c0bd2c5" />



<img width="1496" height="1080" alt="Myshell4" src="https://github.com/user-attachments/assets/ab08df32-ace9-4bfb-b6e2-42da190dd1df" />



<img width="1606" height="1080" alt="Myshell2" src="https://github.com/user-attachments/assets/a87c0d18-38e5-424e-b026-992f996624f6" />



<img width="1572" height="1080" alt="Myshell3" src="https://github.com/user-attachments/assets/67c58dfd-fdfe-4913-bcea-5140dca04edd" />



---

## 🧠 Why This Project?

Most developers use shells daily without understanding how they work internally.  
This project aims to bridge that gap by rebuilding core shell behavior from scratch.

It demonstrates knowledge in:

- Operating Systems fundamentals
- Process management
- Inter-process communication (IPC)
- Software architecture design
- Python systems programming

---

## ⚙️ Features 

### 🧩 Core Shell Features
- Command execution (like Linux terminal)
- Built-in commands support (`cd`, `pwd`, `history`, etc.)
- Modular architecture

---

### 🔗 Advanced Execution
- 🧵 **Pipes (`|`)**
  ```bash
  ls | grep py | sort

⚡ Background Processes (&)

python server.py &

🔁 Multiple Commands (&&)

pwd && ls && echo done

---

### 🧠 System Features

📜 Command history tracking

🔖 Alias support

📝 Command logging system

🧪 Error handling

🧼 Clean CLI experience

🧱 Architecture

---

## The project is fully modular:


myshell/

│

├── main.py

├── shell.py

├── parser.py

├── executor.py

├── shellbuiltins.py

├── processmanager.py

├── pipeline.py

├── history.py

├── aliases.py

├── logger.py

└── config.py

---

## 🧠 How It Works

User enters a command
Input is parsed and analyzed
Shell detects:
Built-in commands
Pipes
Background execution
Execution is handled via subprocesses
Output is returned to terminal

---

## 🔥 Example Usage

myshell:/home/user$ pwd

/home/user



myshell:/home/user$ ls | grep py

main.py

parser.py



myshell:/home/user$ echo hello > file.txt

myshell:/home/user$ cat file.txt

hello



myshell:/home/user$ python server.py &

[BG] PID: 12345


---

## 🧠 Key Concepts Learned

This project strengthens understanding of:

Process creation & management
Unix-like shell architecture
Pipes and IPC (Inter-Process Communication)
Command parsing systems
Background vs foreground execution
System-level thinking in software design

---

## 📈 Project Evolution

v1: Basic command execution

v2: Built-ins + parsing

v3: Pipes, redirection, aliases, history

v4: Background processes, job handling, modular architecture

---

## 🛠️ Tech Stack

Python 3

subprocess module

os module

signal handling (basic level)

---

## 🎯 Future Improvements (v5 roadmap)

Job control (fg, bg)

Advanced parser (quotes, escape chars)

Autocomplete (TAB support)

Arrow key history navigation

Terminal UI improvements

Configuration file (.myshellrc)

Plugin system

---

## 📌 Educational Value

This project is ideal for:

Computer Science students

Systems programming learners

OS course practice

Interview preparation (low-level thinking)


## ⚠️ Disclaimer

This shell is not a production-ready shell, but a learning-oriented implementation of Unix-like behavior for educational purposes.

---

## ⭐ Show Support

If you find this project interesting:

⭐ Star the repo

🍴 Fork it

🧠 Use it to learn systems programming

---

## 👨‍💻 Author

Built by Bakhouche Mohamed Qamar Eddine a Computer Science student exploring Systems Programming, Operating Systems, and Low-level software design.
