"""
Create the necessary output folders.
"""

from os import mkdir


def create_output_folders(path: str, categories: dict):
    """Create folders for csv and jpg files."""
    mkdir(path)
    mkdir(f"{path}/images")
    mkdir(f"{path}/information")
    for key in categories.keys():
        mkdir(f"{path}/images/{key}")
