#!python3
import os

import pyperclip
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    name= input("Provide variable name to add to the .env file:")
    with open(os.getenv("ENV_LOCATION"), "a")as file:
        file.write(f'\n{name.upper().replace(" ", "_")}="{pyperclip.paste().replace("\\", "/")}"')