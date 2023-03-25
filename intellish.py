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
    print(Fore.BLUE, end="")
    print("---------------------------------------------------------------------------------------------------------")
    print()
    print("Welcome to the ML Terminal Interface!")
    print("This interface allows you to execute bash commands and navigate the file system.")
    print("You can use the following commands:")
    print("  H:            Print this help message.")
    print("  Q:            Quit the terminal interface.")
    print("  C:            Clear the terminal window.")
    print("  Goto <folder>: Navigate to a folder in the current directory. (.. for parent folder)")
    print("")
    print("To execute a bash command, simply type it in and press enter.")
    print("If the command is not recognized as a bash command, the interface will attempt to translate it into one.")
    print("If it cannot translate the command, it will print an error message.")
    print("")
    print("Note: This interface is not a full bash shell, and may not support all bash commands.")
    print()
    print("----------------------------------------------------------------------------------------------------------")
    print(Fore.GREEN, end="")

print_heading()
print_intro()


print()
    
def print_quit():
    """
    Prints a goodbye message and returns.
    """
    print(Fore.BLUE, end="")
    print("Bye!")
    return

while True:
    """
    The main event loop of the program.
    """
    current_folder = os.path.basename(os.getcwd())
    print(Fore.LIGHTGREEN_EX)
    command = input(f"{current_folder} > " + Fore.RESET)
    
    # If command is 'h' show help
    if command.lower() == "h":
        print_help()
        continue
    
    # If command is 'q' quit terminal
    if command.lower() == "q": 
        break
    
    # If command has 'goto' change directory
    if command.lower().startswith("goto"):
        dir = ' '.join(command.split(" ")[1:])
        try:
            os.chdir(dir)
        except:
            print(Fore.RED + "ERROR: No such folder exist"+Fore.GREEN)
        continue
    
    
    # If command is 'c' then clear the screen
    if command.lower() == "c":
        os.system('clear')
        continue
    
    output, err = run_command(command)
    
    # If the normal command gives a error then try to translate it
    if err:
        translated_script = translate_to_command(command)
        print("Translated Script: " + translated_script)
        output, err_2 = run_command(translated_script)

        # If the translated command also gives a error then print error
        if err_2:
            print(Fore.RED + output + Fore.GREEN)
            print(Fore.RED + "ERROR: Sorry We couldn't understand your command." + Fore.GREEN)
            continue
    
    # If the command is valid then print the output
    print(Fore.RESET + f"{output}"+Fore.GREEN)


print_quit()