import os
import colorama
import subprocess
from time import sleep
from colorama import Fore
from ml_terminal_interface import translate_to_command, run_command


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


def print_help():
    print("Welcome to the ML Terminal Interface!")
    print("This interface allows you to execute bash commands and navigate the file system.")
    print("You can use the following commands:")
    print("  H:            Print this help message.")
    print("  Q:            Quit the terminal interface.")
    print("  C:            Clear the terminal window.")
    print("  Goto <folder>: Navigate to a folder in the current directory.")
    print("")
    print("To execute a bash command, simply type it in and press enter.")
    print("If the command is not recognized as a bash command, the interface will attempt to translate it into one.")
    print("If it cannot translate the command, it will print an error message.")
    print("")
    print("Note: This interface is not a full bash shell, and may not support all bash commands.")

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
        print_help()
        continue
    
    if command.lower() == "q": 
        break
    
    if command.lower().startswith("goto"):
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
    
    output, err = run_command(command)
    
    if err:
        translated_script = translate_to_command(command)
        output, err_2 = run_command(translated_script)


        if err_2:
            print(Fore.RED + output + Fore.GREEN)
            print(Fore.RED + "ERROR: Sorry We couldn't understand your command." + Fore.GREEN)
            continue
    
    
    print(f"{output}")
    print(Fore.GREEN)

print_quit()