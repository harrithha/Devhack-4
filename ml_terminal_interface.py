import subprocess
import colorama
from colorama import Fore
import openai
import os
import sys

openai.api_key = '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'

messages = [
        {"role": "system", "content": "You are a helpful assistant."},
]
message = "hi"
messages.append(
                {"role": "user", "content": message},
        )
chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
)
print(chat_completion.choices[0].message.content)


def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True, check=None, stderr=subprocess.PIPE)

    #Returning error incase of error
    if len(result.stderr) > 0:
        print(Fore.RED + "ERROR: ", end=" ")
        return result.stderr.decode().strip()
    
    #Returning output
    return result.stdout.decode().strip()

def translate_to_command(command: str):
    message = command
    message = "Give only the bash command to " + message + "without any other descriptive text"
    if message:
        messages.append(
                {"role": "user", "content": message},
        )
        chat_completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
        )
    answer = chat_completion.choices[0].message.content
    print(answer)
    nw = answer.split("```")[0]
    messages.append({"role": "assistant", "content": nw})
    return f"{nw}"


    