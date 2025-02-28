#!python3

import webbrowser
import os
from dotenv import load_dotenv
import time
from PIL import ImageGrab, ImageChops
import pyautogui



def check_diff(box):
    img = ImageGrab.grab(bbox=box)
    # img.save("check2.png")
    i = int()
    while i !=20:
        img2 = ImageGrab.grab(bbox=box)
        if ImageChops.difference(img, img2).getbbox():
            # img2.save("check3.png")
            break
        else:
            i+=1
            # print("It is same")
            time.sleep(1)


if __name__ == "__main__":
    load_dotenv()
    sitelink= f"https://yandex.com/images"
    webbrowser.get(f'"{os.getenv("BROWSER_PATH")}" --private %s').open(sitelink)
    time.sleep(3)
    check_diff((127, 56, 154, 81))
    pyautogui.hotkey("ctrl", "v")

