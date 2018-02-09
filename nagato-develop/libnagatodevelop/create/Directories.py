
import os
from pathlib import Path

DIRECTORIES = [
    "", 
    "debian",
    "debian/source",
    "{}",
    "{}/dialog",
    "{}/dialog/label",
    "{}/eventbox",
    "{}/menu",
    "{}/menu/context",
    "{}/resources",
    "{}/resources/images",
    "readme_extra"
    ]

class NagatoDirectories(object):

    def initialize(self, library_name, project_directory):
        for yuki_directory in DIRECTORIES:
            yuki_directory = yuki_directory.format(library_name)
            yuki_path = Path(os.path.join(project_directory, yuki_directory))
            yuki_path.mkdir(parents=True)

    def __init__(self):
        pass
