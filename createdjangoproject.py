#!python3

import os
from dotenv import load_dotenv
import subprocess
import sys

load_dotenv()
# print(os.getenv("ENTRYPOINT_DATA"))
# print(os.getenv("DIR_LOCATION"))
# print(os.getenv("DOCKERFILE_DATA").replace("\\n", "\n"))
# print(os.getenv("MODULE_NAMES"))
# print(os.getenv("SQL_DATA"))


if __name__ == "__main__":
    os.chdir(os.getenv("DIR_LOCATION"))
    dir_name= input("Provide the name of the project: ").title()
    os.makedirs(f"{dir_name}/Backend", exist_ok=True)
    os.chdir(f"{dir_name}/Backend")

    try:
        import django
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "django"])

    subprocess.run([sys.executable, "-m", "django", "startproject", "Backend", "."])

    with open(".gitignore", "w") as file:
        file.write(".env")

    with open(".dockerignore", "w") as file2:
        file2.write(".env\n.gitignore")

    # i fucking hate this shit, even though i'm using \ it is recognised as \\ but only prints \ even in terminal
    with open("Dockerfile", "w") as file3:
        file3.write(os.getenv("DOCKERFILE_DATA").replace("\\n", "\n"))

    with open("entrypoint.sh", "w") as file4:
        file4.write(os.getenv("ENTRYPOINT_DATA"))

    # this is used to create a database and user for docker container as it throws an error everytime i try doing it from docker-compose
    os.mkdir("init-scripts")
    with open("init-scripts/create_db.sql", "w") as file5:
        file5.write(os.getenv("SQL_DATA"))

    # i suggest copying the docker-compose file yourself due to how indentation sensitive and long that shit is
    # i could copy and paste that shit right now i dont know whether ill do that or not
    with open("docker-compose.yml", "w") as file6:
        file6.write(os.getenv("COMPOSE_DATA").replace("\\n", "\n"))

    with open("requirements.txt", "w") as file7:
        file7.write(os.getenv("MODULE_NAMES"))