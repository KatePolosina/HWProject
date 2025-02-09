import os
import shutil


def get_folder():
    """Имя папки в которой вы находитесь"""
    get_f = os.path.basename(os.getcwd())
    print(f'Вы находитесь в папке: {get_f}')
