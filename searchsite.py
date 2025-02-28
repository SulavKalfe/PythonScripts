#!python3

import webbrowser
import pyperclip

if __name__ == "__main__":
    # remember pyperclip will use the last thing you've copied it doesn't have your clipboard history
    webbrowser.open(pyperclip.paste())
