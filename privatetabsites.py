#!python3

import webbrowser
import sys
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    # i did this cause webbrowser doesn't recognise opera gx as a browser. if you use browsers such as chrome, edge
    # or firefox the proper way of using this is
    # webbrowser.get(f'"browsername" --what the private mode is called %s').open(site)
    # remember the browsername should be in quotation marks otherwise it won't recognise .exe
    # now if you're like me and use browser that webbrowser doesn't recognise find the browser's exe file
    # for me it was located inside C:\Users\username\AppData\Local\Programs\browsername
    # it'll most likely be same for you
    # copy the path with the .exe too not just the folder path
    load_dotenv()
    links= os.getenv("SITE_LINKS").replace("\n", "").split(";")
    # print(links)
    site= sys.argv[1]
    webbrowser.get(f'"{os.getenv("BROWSER_PATH")}" --private %s').open(links[int(site)])
