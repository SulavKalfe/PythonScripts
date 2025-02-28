#!python3

import webbrowser
import os
from dotenv import load_dotenv
import pyperclip

if __name__ == "__main__":
    load_dotenv()
    # idk which of these things are required for google to work but this shit work fine for me so i won't change it
    sitelink= f"https://www.google.com/search?client=opera-gx&q={pyperclip.paste().replace(" ", "+")}"
    webbrowser.get(f'"{os.getenv("BROWSER_PATH")}" --private %s').open(sitelink)
