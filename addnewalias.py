from dotenv import load_dotenv
import pyperclip
import os

load_dotenv()
cmdname= input("Give the command name: ")
cmdfullname= input("Give command's full name: ")
addbgmode= input("Write Y for background mode or anything else for other mode: ")
with open(os.getenv("ALIAS_LOCATION"), "a") as file:
    file.write("\n")
    file.write(f"REM {cmdname}= {cmdfullname}\n")
    if addbgmode.lower()== "y":
        file.write(f"doskey {cmdname}={pyperclip.paste()}.py ^& exit\n")
    else:
        file.write(f"doskey {cmdname}={pyperclip.paste()}.py\n")


with open(os.getenv("ENV_LOCATION"), "r") as file2:
    shit= file2.readlines()

for index, i in enumerate(shit):
    if i.__contains__("EXCLUDE_CMD"):
        # print(i)
        fuck= list(i)
        fuck.insert(-2, f";{cmdname}")
        shit[index]= "".join(fuck)
        # print(len(i))

with open("C:/Users/ASUS TUF F15/Documents/Scripts/check.txt", "w") as file3:
    file3.write("".join(shit))
