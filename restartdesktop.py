import time
import os
import sys

if __name__== "__main__":
    time.sleep(3)
    os.system(f"shutdown /{sys.argv[1]} /t 1")