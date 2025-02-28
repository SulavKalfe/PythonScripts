import os
from dotenv import load_dotenv

load_dotenv()
with open(os.getenv("ALIAS_LOCATION"), "r") as file:
    a= file.readlines()
# print(a)
for i in a:
    if i.__contains__("doskey"):
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
