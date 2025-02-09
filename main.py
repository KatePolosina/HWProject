import os
import shutil





def del_file(file):
    """Удаление файла"""
    if os.path.exists(file):
        os.remove(file)
        print(f'Файл {file} удален')
    else:
        print(f'Файл {file} не найден')


