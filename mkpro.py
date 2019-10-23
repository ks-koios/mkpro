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

def git_setup(github_user, github_token, project_name):
    subprocess.call(["git", "init"])

    with open(".gitignore", "w+") as f:
        f.write("venv/")

    with requests.Session() as session:
        session.auth = ('token', github_token)

        resp = session.post(
            "https://api.github.com/user/repos",
            headers = {"Accept": "application/vnd.github.inertia-preview+json"},
            json = {"name": project_name}
        )
    print(resp)
    print(json.dumps(resp.json(), indent=4))

def create_venv(full_path):
    subprocess.call(["py", "-m", "venv", "venv"])
    print("## Created virtual environment")


# TODO(5): open up code in WSL

if __name__ == "__main__":
    settings = read_settings()
    project_name = input("## Enter the project name: ")
    full_path = settings["rootFolderPath"].rstrip('/') + '/' + project_name
    create_project_folder(full_path)
    os.chdir(full_path)
    git_setup(settings["githubUser"], settings["githubToken"], project_name)
    # create_venv(full_path)
    
