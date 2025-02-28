#!python3

import os
import pyperclip
import sys
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    option= sys.argv[1]
    with open(os.getenv("ENV_LOCATION"), "r") as file:
        var = file.readlines()

    for i in var:
        if i.__contains__("CONTINUE") and int(option)==0:
            var[var.index(i)+1]= pyperclip.paste()+'\n'
        elif i.__contains__("CONTINUE") and int(option)==1:
            var[var.index(i)+2]= pyperclip.paste()+'\n'

    with open(os.getenv("ENV_LOCATION"), "w") as file:
        file.write("".join(var))
