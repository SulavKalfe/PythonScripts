#!python3

import webbrowser
import os
from dotenv import load_dotenv
import pyperclip

if __name__ == "__main__":
    load_dotenv()
    sitelink= f"https://duckduckgo.com/?q={pyperclip.paste().replace(" ", "+")}&t=opera&ia=web"
    webbrowser.get(f'"{os.getenv("BROWSER_PATH")}" --private %s').open(sitelink)
