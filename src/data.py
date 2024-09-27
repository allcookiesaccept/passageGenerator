import os
from settings import BASE_DIR

folder_path = os.path.join(BASE_DIR, 'src')

with open(f"{os.path.join(folder_path, 'anchors.txt')}", 'r') as file:
    anchors = file.read().splitlines()

