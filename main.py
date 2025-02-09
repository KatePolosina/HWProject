import os
import shutil




def couter (dir=os.getcwd()):
    """Считает количество вложенных папок и файлов"""
    dir = dir
    if not os.path.isdir(dir):
        print(f'Папка {dir} отсутствует или {dir} не является папкой')
        return
    tree = os.walk(dir)
    total_dirs = 0
    total_files = 0
    for root, dirs, files in tree:
        dirs[:] = [x for x in dirs if not x.startswith('.') and not x.startswith('__')]
        files = [y for y in files if not y.startswith('.')]
        print(f'Папка: {root}')
        total_dirs += len(dirs)
        total_files += len(files)
        print(f'Вложенных папок: {len(dirs)}. Вложенных файлов: {len(files)}')
        print(f'Вложенные папки: {dirs}. Вложенные файлы: {files}')
        print('-'*40)
