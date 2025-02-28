#!python3

import webbrowser
import pyperclip

if __name__ == "__main__":
    # please check the urls before using this cause it looks like there is t=opera check can be another if you use
    # any other browser other than opera ones
    webbrowser.open(f'"https://duckduckgo.com/?q={pyperclip.paste().replace(" ", "+")}&t=opera&ia=web"')
