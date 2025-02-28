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
    sitelink= f"https://translate.google.com/?sl=auto&tl=en&op=images"
    webbrowser.get(f'"{os.getenv("BROWSER_PATH")}" --private %s').open(sitelink)
    time.sleep(3)
    check_diff((127, 56, 154, 81))
    # the diagonal location is the location of the reload button of website it check if it has changed or not
    # and then moves into the other step
    # yes button location is used because i'm doing this in private tab which requires you to give access to it
    # everytime you do it
    # now if you don't close the tab after you close the window it'll break the steps and the translation may not happen
    # so you should check if yes button appears or not
    # check if those positions are different for you or not
    # diagonal location 1(127, 56)
    # diagonal location2(154, 81)
    # yes button location(494, 271)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.moveTo(494, 271, duration=1)
    pyautogui.click()

