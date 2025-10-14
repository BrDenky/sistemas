# First Exercise - Mateo Pilaquinga
import os
import sys

def star_proc(n, num_proc=1):   
    pid = os.getpid()
    ppid = os.getppid()
    
    # If it is the first process, it is the parent.
    if num_proc == 1:
        print(f"[Parent] pid={pid}  ppid={ppid}  children_expected={n-1}")
        
        # We create n-1 child processes
        for i in range(1, n):
            fork_pid = os.fork()
            if fork_pid == 0:
                # Child Process
                print(f"[Child {i}] pid={os.getpid()}  ppid={os.getppid()}")
                sys.exit(0)
        
        # The father waits for all the children to finish
        for i in range(n - 1):
            os.wait()
    else:
        print(f"[Child {num_proc}] pid={pid}  ppid={ppid}")

def main():
    try:
        user = input("How many processes to create (including the parent)? n = ")
        n = int(user)
        
        if n < 1:
            print("The number of processes must be at least 1")
            return
        
        star_proc(n)
        
    except ValueError:
        print("Please enter a valid number")
    except KeyboardInterrupt:
        print("\nProgram interrupted")

if __name__ == "__main__":
    main()