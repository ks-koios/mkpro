import json
import os

def read_settings():
    with open("settings.json", "r") as settings_file:
        settings = json.load(settings_file)
        return settings

def create_project_folder(folder_path, project_name):
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

# TODO(1): create a venv
def create_venv():
    pass
# TODO(2): git init
# TODO(3): .gitignore
# TODO(4): git push
# TODO(5): open up code in WSL

if __name__ == "__main__":
    settings = read_settings()
    project_name = input("## Enter the project name: ")
    create_project_folder(settings["RootFolderPath"], project_name)
