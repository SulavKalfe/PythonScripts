#!python3

import webbrowser
import os
from dotenv import load_dotenv
import pyperclip

if __name__ == "__main__":
    load_dotenv()
    # check websites.py for why webbrowser has this param
    # pyperclip will check your last copied or cut from the clipboard and open in the browser so you dont have to copy paste
    webbrowser.get(f'"{os.getenv("BROWSER_PATH")}" --private %s').open(pyperclip.paste())