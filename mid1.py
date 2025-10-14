import os
import sys

def create_processes(n, process_num=1):
    """
    Crear n procesos donde 1 es el parent y n-1 son children.
    
    Args:
        n: número total de procesos a crear
        process_num: número actual del proceso
    """
    
    pid = os.getpid()
    ppid = os.getppid()
    
    # Si es el primer proceso, es el padre
    if process_num == 1:
        print(f"[Parent] pid={pid}  ppid={ppid}  children_expected={n-1}")
        
        # Crear n-1 procesos hijo
        for i in range(1, n):
            fork_pid = os.fork()
            if fork_pid == 0:
                # Proceso hijo
                print(f"[Child {i}] pid={os.getpid()}  ppid={os.getppid()}")
                sys.exit(0)
        
        # El padre espera a que terminen todos los hijos
        for i in range(n - 1):
            os.wait()
    else:
        print(f"[Child {process_num}] pid={pid}  ppid={ppid}")

def main():
    """Función principal del programa."""
    try:
        user_input = input("How many processes to create (including the parent)? n = ")
        n = int(user_input)
        
        if n < 1:
            print("El número de procesos debe ser al menos 1")
            return
        
        create_processes(n)
        
    except ValueError:
        print("Por favor, ingresa un número válido")
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")

if __name__ == "__main__":
    main()