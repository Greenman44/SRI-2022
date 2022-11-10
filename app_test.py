from library.parser import parse_dataset_from_path
from pathlib import Path
import pandas as pd


file = Path(r'D:\Cibernética\!!!!Tercer año\SRI\20news-bydate-train')

data = parse_dataset_from_path(file, "20NewGroups")




print(data)