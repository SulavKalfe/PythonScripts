#!python3

import subprocess
from dotenv import load_dotenv
import os

load_dotenv()
# so i tried using subprocess.Popen but it would throw an error saying something like win32 apps can't be opened or
# something that's why i had to use this method it does open all the app i want so no worries about it
# although i don't exactly know how subprocess.run works other is just standard list compression and replacing escape
# with slash so that the path can be found although it may work if i haven't done that but at this point i'm too lazy to
# check, and it works so it fine for me
# and atlast i'm using semicolon to seperate the path as there are multiple path in a single variable

# i genuinely don't know why pycharm won't run when using this method but at this point im too done with this to check
# so fuck it im using subprocess.Popen it
[subprocess.run(["start","", i], shell=True) for i in os.getenv("APP_PATH").replace("\n", "").split(";")]
subprocess.Popen(os.getenv("APP_PATH2"))
