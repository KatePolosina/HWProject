import os
import shutil






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


