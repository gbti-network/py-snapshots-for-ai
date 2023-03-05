import os
import json
import chardet

from snapshots.py.obfuscate_json import obfuscate_sensitive_data

# Define whether to obfuscate sensitive data in JSON files
OBFUSCATE_SENSITIVE_DATA = True

def add_file_blocks(hierarchy, md_file, base_dir):
    """
    Given a hierarchical array of files and folders and an action to perform, this function loops through all the files
    in the hierarchy, starting from the topmost level, and performs the specified action on each file.
    :param hierarchy: The hierarchical array to loop through
    :param action: The action to perform on each file
    :param base_dir: The base directory for the hierarchy
    """
    for item in hierarchy:
        if isinstance(item, str):
            # Perform the action on the file
            file_path = os.path.join(base_dir, item)
            add_file_to_md(file_path, md_file)
        elif isinstance(item, dict):
            folder_name = list(item.keys())[0]
            # Loop through the files in the folder
            for file_item in item[folder_name]:
                if isinstance(file_item, str):
                    # Perform the action on the file
                    file_path = os.path.join(base_dir, folder_name, file_item)
                    add_file_to_md(file_path, md_file)
                elif isinstance(file_item, dict):
                    # Recursively loop through subfolders
                    add_file_blocks([file_item], md_file, os.path.join(base_dir, folder_name))






def add_file_to_md(file_path, md_file):
    """
    Given a file path and a markdown file object, this function reads the contents of the file, obfuscates sensitive
    data in JSON files, and writes the file contents to the markdown file object in a code block.
    :param file_path: The path to the file to add to the markdown file
    :param md_file: The markdown file object to add the file to
    """

    filename = os.path.basename(file_path)
    file_path_with_parent = os.path.join('..', file_path)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            contents = f.read()
    except UnicodeDecodeError:
        print(f"Skipping file {file_path} because it is not UTF-8 encoded.")
        return

    file = {"filepath": file_path, "contents": contents}

    # Obfuscate sensitive data if necessary and if the file is not an example file
    if OBFUSCATE_SENSITIVE_DATA and filename.endswith(".json") and "-example" not in filename:
        file['contents'] = obfuscate_sensitive_data(json.loads(file['contents']))

    # Write the file blocks to the markdown file
    md_file.write(f"## {file['filepath']}\n")
    md_file.write(f"```\n")
    md_file.write(f"{file['contents']}\n")
    md_file.write(f"```\n\n")
