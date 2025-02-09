import os
import shutil

def get_path():
    """Путь до папки в которой вы сейчас находитесь"""
    get_p = os.getcwd()
    print(f'Путь до папки, в которой вы находитесь: {get_p}')
    return get_p



