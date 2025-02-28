#!python3

import os
import webbrowser
from dotenv import load_dotenv
import sys

if __name__ == "__main__":
    load_dotenv()
    sitelink= os.getenv("CONTINUE").replace("\n", "").split(";")
    # print(sitelink)
    option= sys.argv[1]
    webbrowser.open(sitelink[int(option)])