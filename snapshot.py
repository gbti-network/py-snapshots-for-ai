import os
import datetime
import pyperclip
import json

from snapshots.py.hierarchy import build_hierarchy
from snapshots.py.hierarchy import filter_hierarchy
from snapshots.py.hierarchy import print_hierarchy
from snapshots.py.md_output import add_file_blocks

AI_MODE_INTRO = "Hi, please consider this markdown file as the lastest iteration of my application. The file structure and code contained within should be considered the most updated version of all files and file structures. Once you read this markdown summary, please summarize anything notable that is new to you compared to our past work together."
SNAPSHOTS_DIR = "./snapshots/captures/"
PY_SNAPSHOTS_DIR = os.path.join(SNAPSHOTS_DIR, "py")
IGNORE_PATTERNS = ["package", ".idea","node_modules",".git","pycache",'captures','requirements']

def generate_md_file():
    """
    Generates a markdown file that lists every file in the current directory
    and shows the contents of that file in a code block.

    Ignores files and directories specified in the .gitignore file.

    """
    # Create the snapshots directory if it does not exist
    if not os.path.exists(SNAPSHOTS_DIR):
        os.makedirs(SNAPSHOTS_DIR)

    if not os.path.exists(PY_SNAPSHOTS_DIR):
        os.makedirs(PY_SNAPSHOTS_DIR)

    # Get the directory structure
    hierarchy = build_hierarchy('.')
    hierarchy = filter_hierarchy(hierarchy,IGNORE_PATTERNS)

    # Print the directory structure
    hierarchy_output = print_hierarchy(hierarchy)

    # Get the current date and time
    now = datetime.datetime.now()
    timestamp = now.strftime("%m-%d-%Y-%H_%M_%S-%z")

    # Create the markdown file name
    md_filename = f"snapshot-{timestamp}.md"
    md_path = os.path.join(SNAPSHOTS_DIR, md_filename)

    # Open the markdown file for writing
    with open(md_path, "w", encoding="utf-8") as md_file:
        # Write the header
        md_file.write(AI_MODE_INTRO)
        md_file.write("\n\n")

        md_file.write("# Project Structure\n\n")

        md_file.write(hierarchy_output)
        md_file.write("\n\n")

        md_file.write("# Project Files\n\n")

        add_file_blocks(hierarchy , md_file , '.')

    # Copy the markdown file to the clipboard
    pyperclip.copy(md_path)

    print("Snapshot generated.")


if __name__ == "__main__":
    generate_md_file()
