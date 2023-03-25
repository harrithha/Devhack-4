import os
import subprocess
from time import sleep
from ml_terminal_interface import translate_to_command, run_command
import colorama
from colorama import Fore


def print_heading():
    print(Fore.BLUE)
    print("--------------------------------------------------------------------------")
    print("|    _____ _   _ _______ ______ _      _      _____      _____ _    _    |")
    print("|   |_   _| \ | |__   __|  ____| |    | |    |_   _|    / ____| |  | |   |")
    print("|     | | |  \| |  | |  | |__  | |    | |      | |_____| (___ | |__| |   |")
    print("|     | | | . ` |  | |  |  __| | |    | |      | |______\___ \|  __  |   |")
    print("|    _| |_| |\  |  | |  | |____| |____| |____ _| |_     ____) | |  | |   |")
    print("|   |_____|_| \_|  |_|  |______|______|______|_____|   |_____/|_|  |_|   |")
    print("|                                                                        |")
    print("--------------------------------------------------------------------------")
    print(Fore.GREEN)
    

def print_intro():
    print(Fore.BLUE)
    print("--------------------")
    print("Enter H: for help")
    print("Enter Q: to Quit")
    print("Enter C: to Clear")
    print("Enter Goto <folder>: to go to folder (.. for parent folder))")
    print("--------------------")
    print(Fore.GREEN)
    

print_heading()
print_intro()


print()
    
def print_quit():
    print("Bye!")
    return

while True:
    current_folder = os.path.basename(os.getcwd())
    command = input(f"{current_folder}) ")
    
    if command.lower() == "h":
        print("TODO: HELP")
        continue
    
    if command.lower() == "q": 
        break
    
    if command.lower().startswith("goto"):
        # changing dir
        dir = ' '.join(command.split(" ")[1:])
        try:
            os.chdir(dir)
        except:
            print(Fore.RED)
            print("ERROR: No such folder exist")
            print(Fore.GREEN)
        continue
    
    if command.lower() == "c":
        os.system('clear')
        continue
    
    # translated_script = translate_to_command(command)
    # print(f"Bash: {translated_script}")
    # output = run_command(translated_script)
    output = run_command(command)
    print(f"{output}")
    print(Fore.GREEN)

print_quit()