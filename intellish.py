import os
import subprocess
from time import sleep
from ml_terminal_interface import translate_to_command, run_command


current_folder = os.path.basename(os.getcwd())

def print_intro():
    print("--------------------")
    print("Enter H: for help")
    print("Enter Q: to Quit")
    print("Enter C: to Clear")
    print("--------------------")

print_intro()


print()
    
def print_quit():
    print("Bye!")
    return

while True:
    command = input(f"{current_folder}) ")
    
    if command.lower() == "h":
        print("TODO: HELP")
        continue
    
    if command.lower() == "q": 
        break
    
    if command.lower() == "c":
        command = "clear"
    
    output = run_command(command)
    print(output)

print_quit()