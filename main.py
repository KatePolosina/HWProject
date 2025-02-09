import os
import re

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

