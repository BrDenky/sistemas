# Second Exercise - Mateo Pilaquinga
import os
import sys

def chain_process(n, current_process=1):    
    pid = os.getpid()
    ppid = os.getppid()
    
    # We show information about the current process
    if current_process == 1:
        expected = 1 if n > 1 else 0
        print(f"[Parent] pid={pid}  ppid={ppid}  children_expected={expected}", flush=True)
    else:
        print(f"[Child {current_process-1}] pid={pid}  ppid={ppid}  children_expected={'1' if current_process < n else '0'}")
    
    # If we have not yet created all the processes in the chain
    if current_process < n:
        fork_pid = os.fork()
        
        if fork_pid == 0:
            # Child process: continues the chain by creating its own child
            chain_process(n, current_process + 1)
            sys.exit(0)
        else:
            # Parent process: waits for the child to finish
            os.waitpid(fork_pid, 0)

def main():
    try:
        input_n = input("How many processes to create (including the parent)? n = ")
        n = int(input_n)
        
        if n < 1:
            print("The number of processes must be at least 1")
            return
        
        chain_process(n)
        
    except ValueError:
        print("Please enter a valid number")
    except KeyboardInterrupt:
        print("\nProgram interrupted")

if __name__ == "__main__":
    main()