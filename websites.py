#!python3

import webbrowser
import sys
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    links= os.getenv("SITE_LINKS").replace("\n", "").split(";")
    # print(links)
    site= sys.argv[1]
    webbrowser.open(links[int(site)])