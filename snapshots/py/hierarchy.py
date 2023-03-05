import os


def build_hierarchy(root_dir):
    """
    Given a directory location, this function iterates through all files and folders in that directory creating a
    hierarchical array of files and folders.
    :param root_dir: The directory to start building the hierarchy from
    :return: A list representing the hierarchy of files and folders in root_dir
    """
    hierarchy = []
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isfile(item_path):
            hierarchy.append(item)
        elif os.path.isdir(item_path):
            hierarchy.append({item: build_hierarchy(item_path)})
    return hierarchy


def filter_hierarchy(hierarchy, patterns):
    """
    Given a hierarchical array of files and folders and an array of string patterns, this function iterates through the
    hierarchy and removes any object whose file name or folder name contains one of the strings in patterns.
    :param hierarchy: The hierarchical array to filter
    :param patterns: An array of string patterns to filter with
    :return: A new hierarchical array with the filtered items removed
    """

    filtered_hierarchy = []
    if not hierarchy:
        return filtered_hierarchy
    for item in hierarchy:
        if isinstance(item, str):
            if not any(pattern in item for pattern in patterns):
                filtered_hierarchy.append(item)
        elif isinstance(item, dict):
            filtered_dict = {}
            for key in item.keys():
                if not any(pattern in key for pattern in patterns):
                    filtered_dict[key] = filter_hierarchy(item[key], patterns)
            if filtered_dict:
                filtered_hierarchy.append(filtered_dict)
    return filtered_hierarchy



def print_hierarchy(hierarchy = [] , indent=0):
    """
    Given a hierarchical array of files and folders, this function prints the hierarchy in the desired format and returns
    it as a string.
    :param hierarchy: The hierarchical array to print
    :param indent: The number of spaces to indent each level of the hierarchy
    :return: The hierarchical array as a string
    """
    output = ""
    for item in hierarchy:
        if isinstance(item, str):
            output += f"{' ' * indent}- {item}\n"
        elif isinstance(item, dict):
            folder_name = list(item.keys())[0]
            output += f"{' ' * indent}+ {folder_name}/\n"
            output += print_hierarchy(item[folder_name], indent=indent + 2)
    return output

