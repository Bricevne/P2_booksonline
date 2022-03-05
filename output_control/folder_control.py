"""
Create the necessary output folders.
"""

import os

def create_output_folders(categories: dict):
    """Create folders for csv and jpg files."""
    os.mkdir("products")
    os.mkdir("products/images")
    os.mkdir("products/information")
    for key in categories.keys():
        os.mkdir(f"products/images/{key}")


