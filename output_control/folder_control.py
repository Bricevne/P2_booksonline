"""
Create the necessary output folders.
"""

from os import mkdir
from shutil import rmtree

def create_output_folders(path: str, categories: dict):
    """Create folders for csv and jpg files."""
    mkdir(path)
    mkdir(f"{path}/images")
    mkdir(f"{path}/information")
    for key in categories.keys():
        mkdir(f"products/images/{key}")

def delete_ouput_folders(path: str):
    """Delete all output folders."""
    rmtree(path)

