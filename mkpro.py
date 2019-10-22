import json
import os
import subprocess
import requests

def read_settings():
    with open("settings.json", "r") as settings_file:
        settings = json.load(settings_file)
        return settings

def create_project_folder(full_path):
    if not os.path.isdir(full_path):
        try:
            os.mkdir(full_path)
        except OSError:
            print(f"ERR: Failed creating project directory: {full_path}")
        else:
            print("## Created new project folder")
    else:
        print("## ERR: Project folder already exists")

def create_venv(full_path):
    os.chdir(full_path)
    subprocess.call(["py", "-m", "venv", "venv"])
    print("## Created virtual environment")

# TODO(2): git init
# TODO(3): .gitignore and Readme
# TODO(4): git push
def git_setup(github_token):
    pass
# TODO(5): open up code in WSL

if __name__ == "__main__":
    settings = read_settings()
    project_name = input("## Enter the project name: ")
    full_path = settings["rootFolderPath"].rstrip('/') + '/' + project_name
    create_project_folder(full_path)
    create_venv(full_path)
    git_setup(settings["githubToken"])
    
