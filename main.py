import os
import shutil





def move_obj(src, dst):
    """Перемещение файла или папки"""
    if os.path.isfile(src):
        print(f'Файл {src} перемещен в папку {dst}')
    elif os.path.isdir(src):
        print(f'Папка {src} перемещена в папку {dst}')
    shutil.move(src, dst)
