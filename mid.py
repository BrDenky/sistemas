import os
import sys

def fail(msg: str, code: int = 1) -> None:
    """Imprime un error y termina con código de salida no cero."""
    print(f"Error: {msg}", file=sys.stderr, flush=True)
    sys.exit(code)

def main() -> None:
    # --- Entrada del usuario ---
    try:
        n_str = input("How many processes to create (including the parent)? n = ")
        n = int(n_str)
    except Exception:
        fail("Invalid input (must be an integer).")

    if n < 1:
        fail("n must be >= 1 (includes the initial parent).")

    parent_pid = os.getpid()
    children_to_create = n - 1

    # --- Creación de hijos directos ---
    for i in range(1, n):  # i = 1..(n-1)
        try:
            pid = os.fork()
        except OSError as e:
            fail(f"fork() failed: {e}")

        if pid == 0:
            # Proceso hijo: imprime su info y termina.
            print(f"[Child {i}] pid={os.getpid()}  ppid={os.getppid()}", flush=True)
            # Importante: terminar sin ejecutar código del padre.
            os._exit(0)

    # --- Proceso padre: imprime su info y espera a los hijos ---
    print(f"[Parent] pid={parent_pid}  ppid={os.getppid()}  children_expected={children_to_create}", flush=True)

    reaped = 0
    # Recolecta a todos los hijos para evitar zombis.
    while True:
        try:
            wpid, status = os.wait()
            reaped += 1
        except ChildProcessError:
            # No quedan hijos por esperar.
            break

    if reaped != children_to_create:
        print(f"[Parent] Warning: expected to reap {children_to_create} children but reaped {reaped}.",
              file=sys.stderr, flush=True)

if __name__ == "__main__":
    main()
