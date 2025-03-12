import os
from dotenv import load_dotenv

load_dotenv()
excludecmd= os.getenv("EXCLUDE_CMD").split(";")
# print(excludecmd)

with open(os.getenv("ALIAS_LOCATION"), "r") as file:
    a= file.readlines()
# print(a)
for i in a:
    if i.__contains__("doskey") and not i.__contains__("/b") and i[i.index(" ")+1:i.index("=")] not in excludecmd:
        # print(i)
        index= a.index(i)
        frontpart= i[:i.index("=")+1]
        if i.__contains__("\n"):
            backpart= i[i.index("=")+1:-1]
            a[index]=f"{frontpart}start /b {backpart} ^& exit\n"
            # print(backpart)
        else:
            backpart = i[i.index("=") + 1:]
            a[index] = f"{frontpart}start /b {backpart} ^& exit"
            # print(backpart)

with open(os.getenv("ALIAS_LOCATION"), "w") as file:
    file.write("".join(a))
# print(a)
