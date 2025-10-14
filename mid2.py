import os
import sys

def create_chain_processes(n, current_process=1):
    """
    Crear una cadena de n procesos donde cada proceso crea exactamente un hijo.
    
    Args:
        n: número total de procesos a crear en la cadena
        current_process: número actual del proceso en la cadena
    """
    
    pid = os.getpid()
    ppid = os.getppid()
    
    # Mostrar información del proceso actual
    if current_process == 1:
        print(f"[Parent] pid={pid}  ppid={ppid}  children_expected=1")
    else:
        print(f"[Child {current_process-1}] pid={pid}  ppid={ppid}  children_expected={'1' if current_process < n else '0'}")
    
    # Si aún no hemos creado todos los procesos en la cadena
    if current_process < n:
        fork_pid = os.fork()
        
        if fork_pid == 0:
            # Proceso hijo: continúa la cadena creando su propio hijo
            create_chain_processes(n, current_process + 1)
            sys.exit(0)
        else:
            # Proceso padre: espera a que termine el hijo
            os.waitpid(fork_pid, 0)

def main():
    """Función principal del programa."""
    try:
        user_input = input("How many processes to create (including the parent)? n = ")
        n = int(user_input)
        
        if n < 1:
            print("El número de procesos debe ser al menos 1")
            return
        
        create_chain_processes(n)
        
    except ValueError:
        print("Por favor, ingresa un número válido")
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")

if __name__ == "__main__":
    main()