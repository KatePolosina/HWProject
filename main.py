import os
import shutil


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

