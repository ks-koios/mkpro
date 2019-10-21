import json
import os

def readSettings():
    with open("settings.json", "r") as settings_file:
        settings = json.load(settings_file)
        return settings

# TODO(1): create a folder
def CreateProjectFolder(folder_path, project_name):
    fullPath = folder_path.rstrip('/') + '/' + project_name
    if not os.path.isdir(fullPath):
        try:
            os.mkdir(fullPath)
        except OSError:
            print(f"ERR: Failed creating project directory: {fullPath}")
        else:
            print("## Created new project folder")
    else:
        print("## ERR: Project folder already exists")

# TODO(2): git init

# TODO(3): .gitignore

# TODO(4): git push

# TODO(5): create a venv

# TODO(6): open up code

if __name__ == "__main__":
    settings = readSettings()
    project_name = input("## Enter the project name: ")
    CreateProjectFolder(settings["RootFolderPath"], project_name)
