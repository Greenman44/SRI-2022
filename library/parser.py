from pathlib import Path 
import json
from os import getcwd

def parse_dataset_from_path(path : str, name : str) -> list[dict]:
    """Parser for datasets coming from a directory

    Args:
        path (str): path of dataset

    Returns:
        list (dict): Keys : ("name", "path", "body")
    """
    finalData = []
    try:
        basePath = Path(path)
    except Exception as e:
        raise(e)
    items_basePath = basePath.iterdir() 
    files = []
    folders = []
    for item in items_basePath:
        if item.is_dir:
            folders.append(item)
        elif item.is_file():
            files.append(item)

    for folder in folders: 
        data = process_folder(folder)
        finalData.extend(data)
    data = process_folder(basePath)
    finalData.extend(data)
    dataset_path = getcwd() + f"\\datasets\\{name}_data.json"
    try:
        with open(dataset_path, 'w') as file:
            data = json.dump(finalData, file, indent=4)
            file.close
    except Exception as e:
        raise(e)

    return "success"


def process_folder(folder : Path) -> list[dict]:
    """convert files into dict and append them to the folder data 

    Args:
        folder (Path): path of current folder

    Returns:
        list (dict): Keys : ("name", "path", "keywords")
    """
    folder_data = []
    files = folder.iterdir()
    for file in files:
        if file.is_dir():
            continue
        data = {
            "name" : file.name,
            "path" : str(file.absolute()),
            "body" : file.read_text() 
        }
        folder_data.append(data)

    return folder_data



