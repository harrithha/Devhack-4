import os
import subprocess
from time import sleep


current_folder = os.path.basename(os.getcwd())

print("==================== INTELLI-sh ====================")


print()

while True:
    print("Type your command: ")
    command = input(f"{current_folder}) ")
    
    print(command)
    print()