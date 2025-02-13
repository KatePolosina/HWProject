import argparse
import function
import os

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

    return parser

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    if args.command == 'get_path':
        function.get_path()
    elif args.command == 'get_folder':
        function.get_folder()
    elif args.command == 'create_folder':
        function.create_folder(args.name)
    elif args.command == 'create_file':
        function.create_file(args.name)
    elif args.command == 'del_folder':
        function.del_folder(args.name)
    elif args.command == 'del_file':
        function.del_file(args.name)
    elif args.command == 'copy_file':
        function.copy_file(args.src)
    elif args.command == 'move_obj':
        function.move_obj(args.src, args.dst)
    elif args.command == 'counter':
        function.counter(args.dir)
    elif args.command == 'find_file_txt':
        function.find_file_txt(args.dir)
    else:
        parser.print_help()
