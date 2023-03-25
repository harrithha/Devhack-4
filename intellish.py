import os
import subprocess
from time import sleep
from ml_terminal_interface import translate_to_command, run_command


current_folder = os.path.basename(os.getcwd())

print("==================== INTELLI-sh ====================")
print("Enter H: for help")


print()

def print_help():
    print("Enter H: for help")
    print("Enter Q: to Quit")

while True:
    command = input(f"{current_folder}) ")
    if command == "Q":
        break
    output = run_command(command)
    print(output)
    print()
    