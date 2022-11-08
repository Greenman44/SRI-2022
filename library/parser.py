from pathlib import Path 


def parse_from_url(url : str) -> dict:
    """Parser for datasets coming from a directory

    Args:
        url (str): url of dataset

    Returns:
        dict: Keys : ("name", "url", "keywords")
    """
    finalData = {}
    try:
        basePath = Path(url)
    except Exception as e:
        raise(e)
    items_basePath = basePath.iterdir() 
    files = []
    folders = []
    for item in items_basePath:
        if item.is_file:
            files.append(item)
        elif item.is_dir:
            folders.append(item)

    for folder in folders: 
        data = process_folder(folder)
        finalData.update(data)
    #TODO : end this method
    #Aqui faltaria revisar la lista de archivos
    # en caso de haber, mandar el directorio de la carpeta en la que estas para el metodo de "process_folder" 

def process_folder(folder : Path) -> dict:
    """convert files into dict and append them to the folder data 

    Args:
        folder (Path): url of current folder

    Returns:
        dict: Keys : ("name", "url", "keywords")
    """
    data = {}
    files = folder.iterdir()
    for file in files:
        content = file.read_text
    #TODO: end this method
    #la idea es recorrer los archivos de la carpeta y leerlos, 
    #luego hacerle split por cambio de linea ("\n")
    #y a partir de ahi quitar palabras repetidas y las stopwords



