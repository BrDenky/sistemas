import os
import time

# Primer fork
pid1 = os.fork()

# Segundo fork
pid2 = os.fork()

# Tercer fork
pid3 = os.fork()

# Identificador único de cada proceso según los valores de retorno
print(
    f"Proceso: PID={os.getpid()}, PPID={os.getppid()}, "
    f"pid1={pid1}, pid2={pid2}, pid3={pid3}"
)

time.sleep(20)  # mantener procesos vivos para inspección
