import subprocess

def translate_to_command(command: str):
    command = "files starting with s"
    return "ls | grep s*"

def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True, check=None, stderr=subprocess.PIPE)

    #Returning error incase of error
    if len(result.stderr) > 0:
        print("ERROR", end=" ")
        return result.stderr.decode().strip()
    
    #Returning output
    return result.stdout.decode().strip()
    