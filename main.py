import os
import shutil

def get_path():
    """Путь до папки в которой вы сейчас находитесь"""
    get_p = os.getcwd()
    print(f'Путь до папки, в которой вы находитесь: {get_p}')
    return get_p

def get_folder():
    """Имя папки в которой вы находитесь"""
    get_f = os.path.basename(os.getcwd())
    print(f'Вы находитесь в папке: {get_f}')

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

def create_file(x='file'):
    """Создание нового файла. Имя файла по умолчанию file"""
    if not x.endswith('.txt'):
        x += '.txt'
    base, ext = os.path.splitext(x)
    file = x
    i = 1
    if os.path.exists(file):
        print(f'Файл {file} существует')
    while os.path.exists(file):
        file = f'{base}_{i}{ext}'
        i += 1
    with open(file, 'w') as f:
        pass
    print(f'Создан новый файл {file}')

def del_folder(folder):
    """Удаление папки"""
    shutil.rmtree(folder)
    print(f'Папка {folder} удалена.')

def del_file(file):
    """Удаление файла"""
    if os.path.exists(file):
        os.remove(file)
        print(f'Файл {file} удален')
    else:
        print(f'Файл {file} не найден')

def copy_file(src):
    """Копирование файла"""
    file = src
    base, ext = os.path.splitext(src)
    i = 1
    if not os.path.exists(file):
        print(f'Файл {file} отсутствует')
        return
    while os.path.exists(file):
        file = f'{base}_копия_{i}{ext}'
        i += 1
    shutil.copy2(src, file)
    print(f'Файл {src} скопирован в {file}')

def move_obj(src, dst):
    """Перемещение файла или папки"""
    if os.path.isfile(src):
        print(f'Файл {src} перемещен в папку {dst}')
    elif os.path.isdir(src):
        print(f'Папка {src} перемещена в папку {dst}')
    shutil.move(src, dst)

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

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-n')


