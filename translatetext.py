#!python3

import webbrowser
import os
from dotenv import load_dotenv
import pyperclip

if __name__ == "__main__":
    load_dotenv()
    sitelink= f"https://translate.google.com/?sl=auto&tl=en&text={pyperclip.paste().replace(" ", "%20")}&op=translate"
    webbrowser.get(f'"{os.getenv("BROWSER_PATH")}" --private %s').open(sitelink)
