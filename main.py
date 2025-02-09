import os
import shutil



def create_folder (x='new_folder'):
    """Создание новой папки. Имя новой папки по умолчанию new_folder"""
    folder = x
    new_folder = folder
    i = 1
    if os.path.exists(folder):
        print(f'Папка {folder} существует')
    while os.path.exists(new_folder):
        new_folder = f'{folder}_{i}'
        i += 1
    os.mkdir(new_folder)
    print(f'Создана папка {new_folder}')

