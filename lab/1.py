# q1_memory_list.py
import os

names = ['pedro', 'matias', 'ruby']
print(f'Original list: {names}')
pid = os.fork()

if pid == 0:  # Hijo
    names.append('child-added')
    print(f"[CHILD ] PID={os.getpid()} id(names)={id(names)} -> {names}")
    os._exit(0)
else:         # Padre
    names.pop()
    names.append('parent-added')
    print(f"[PARENT] PID={os.getpid()} id(names)={id(names)} -> {names}")
    os.waitpid(pid, 0)
