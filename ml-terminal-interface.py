import subprocess

def translate_to_command(command: str):
    command = "files starting with s"
    return "ls | grep s*"

def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
    output = result.stdout.decode().strip()
    return output
    
output = run_command("ls  i*")
print(output)