import os
from pathlib import Path
import logging

project_name = "essay"
list_directory = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/configuration/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/exception/__init__.py",
    f"src/{project_name}/logger/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    "templates/index.html",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
]

for filepath in list_directory:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    
    if filedir != "":
        os.makedirs(filedir, exist_ok= True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
        
    if not (os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}") 
        
    else: 
        logging.info(f"{filename} is already exists")