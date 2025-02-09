import os
import shutil



def del_folder(folder):
    """Удаление папки"""
    shutil.rmtree(folder)
    print(f'Папка {folder} удалена.')


