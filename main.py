import os
import shutil
import re
import argparse

def get_path():
    """Путь до папки в которой вы сейчас находитесь"""
    get_p = os.getcwd()
    print(f'Путь до папки, в которой вы находитесь: {get_p}')
    return get_p

def get_folder():
    """Имя папки в которой вы находитесь"""
    get_f = os.path.basename(os.getcwd())
    print(f'Вы находитесь в папке: {get_f}')

def create_folder(x='new_folder'):
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

def counter (dir=os.getcwd()):
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

def find_file_txt(dir=os.getcwd()):
    regex = re.compile(r'\.txt$')
    for root, dirs, files in os.walk(dir):
        found = True
        for file in files:
            if regex.search(file):
                print(os.path.join(root, file))
                found = True
            if not found:
                print(f'{root}: файлы отсутствуют')


def create_parser():
    parser = argparse.ArgumentParser(description='Менеджер файловой системы')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('get_path', help='Вывести путь к текущей папке')
    subparsers.add_parser('get_folder', help='Вывести имя текущей папки')

    create_folder_parser = subparsers.add_parser('create_folder', help='Создать папку')
    create_folder_parser.add_argument('name', nargs='?', default='new_folder', help='Имя новой папки')

    create_file_parser = subparsers.add_parser('create_file', help='Создать файл')
    create_file_parser.add_argument('name', nargs='?', default='file', help='Имя нового файла')

    del_folder_parser = subparsers.add_parser('del_folder', help='Удалить папку')
    del_folder_parser.add_argument('name', nargs='?', help='Имя папки для удаления')

    del_file_parser = subparsers.add_parser('del_file', help='Удалить файл')
    del_file_parser.add_argument('name', help='Имя файла для удаления')

    copy_file_parser = subparsers.add_parser('copy_file', help='Копировать файл')
    copy_file_parser.add_argument('src', help='Файл для копирования')

    move_obj_parser = subparsers.add_parser('move_obj', help='Переместить объект')
    move_obj_parser.add_argument('src', help='Исходный файл/исходная папка')
    move_obj_parser.add_argument('dst', help='Папка назначения')

    counter_parser = subparsers.add_parser('counter', help='Количество папок/файлов')
    counter_parser.add_argument('dir', nargs='?', default=os.getcwd(), help='Папка, в которой требуется узнать количество папок/файлов')

    find_file_txt = subparsers.add_parser('find_file_txt', help='Поиск файлов .txt')
    find_file_txt.add_argument('dir', nargs='?', default=os.getcwd(), help='Папка для поиска')

    return  parser

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    if args.command == 'get_path':
        get_path()
    elif args.command == 'cget_folder':
        get_folder()
    elif args.command == 'create_folder':
        create_folder(args.name)
    elif args.command == 'create_file':
        create_file(args.name)
    elif args.command == 'del_folder':
        del_folder(args.name)
    elif args.command == 'del_file':
        del_file(args.name)
    elif args.command == 'copy_file':
        copy_file(args.src)
    elif args.command == 'move_obj':
        move_obj(args.src, args.dst)
    elif args.command == 'counter':
        counter(args.dir)
    elif args.command == 'find_file_txt':
        find_file_txt(args.dir)
    else:
        parser.print_help()