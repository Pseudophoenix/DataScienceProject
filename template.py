import os
from pathlib import Path
import logging
project_name="datascience"
list_of_files={
    ".github/workflows/.gtikeep",
    f"scr/{project_name}/__init__.py",# __init__.py to allow it to be used anywhere 
    f"src/{project_name}/components/__init__.py",
    
}