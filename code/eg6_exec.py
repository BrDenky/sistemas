import sys
import os

sys.stdout.write('''Provide program name and args to run like you would in a shell.

Examples:

ls
ls -al
ls -l file1 file2 file3

$ ''')
sys.stdout.flush()

program_and_arguments = sys.stdin.readline().rstrip().split()

program = program_and_arguments[0]
arguments = program_and_arguments[1:]

print("program",program)
print("arguments",arguments)


os.execlp(program, program, *arguments)

sys.stdout.write('I executed a program\n')
sys.stdout.flush()