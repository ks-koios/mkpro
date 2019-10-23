# mkpro

A script to automate the initial creation of small Python projects.  Does the following:
1. Creates the project folder in a root project directory indiciated in settings
1. Sets up git including:
    1. Git init
    1. Creating a .gitignore
    1. Stage the .gitignore
    1. Creating the first commit
    1. Creating the repository on account (token & user should be indiciated in settings)
    1. Add the origin and initial push
1. Creating a Python virtual environment

## Setup
    pip install -r requirements.txt
- Add root project folder, github username and API token to settings.json

