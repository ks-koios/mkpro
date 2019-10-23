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
            print("### Created new project folder")
    else:
        print("### ERR: Project folder already exists")

def git_setup(github_user, github_token, project_name):
    print("### Setting up Git")
    subprocess.run(["git", "init"])

    with open(".gitignore", "w+") as f:
        f.write("venv/")

    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "'first commmit'"])

    with requests.Session() as session:
        session.auth = ('token', github_token)
        response = session.post(
            "https://api.github.com/user/repos",
            headers = {"Accept": "application/vnd.github.inertia-preview+json"},
            json = {"name": project_name}
        )
        print(response)

    subprocess.run(["git",
                    "remote",
                    "add",
                    "origin",
                    f"https://github.com/{github_user}/{project_name}.git"])
    subprocess.run(["git", "push", "-u", "origin", "master"])
    
    print("### Git repo created and first commit pushed")
    
def create_venv(full_path):
    subprocess.call(["py", "-m", "venv", "venv"])
    print("### Created virtual environment")

if __name__ == "__main__":
    settings = read_settings()
    project_name = input("## Enter the project name: ")
    full_path = settings["rootFolderPath"].rstrip('/') + '/' + project_name
    create_project_folder(full_path)
    os.chdir(full_path)
    git_setup(settings["githubUser"], settings["githubToken"], project_name)
    create_venv(full_path)
    subprocess.run(["explorer", "."])
    # TODO(5): open up code in WSL
