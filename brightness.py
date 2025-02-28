#!python3

import screen_brightness_control as sbc
import sys

if __name__ == "__main__":
# unlike sound module this takes integer as an parameter which means you need to provide integer value
    ans= sys.argv[1].lower()
    sbc.set_brightness(int(ans))