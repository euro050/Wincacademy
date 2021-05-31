__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'


import os
import shutil
import zipfile


main_path = os.path.dirname(os.path.realpath(__file__))
cache_path = str(main_path) + '\\cache'

#deel1
def clean_cache():
    os.chdir(main_path)
    if os.path.exists(cache_path):
        shutil.rmtree(cache_path)

    os.mkdir(cache_path)

#deel2
def cache_zip(source, target):
    with zipfile.ZipFile(source, 'r') as zipObj:
        zipObj.extractall(target)

#deel3
def cached_files():
    os.chdir(cache_path)
    for root, dirs, files in os.walk('.'):
        files_list = [os.path.abspath(name) for name in files]

    return files_list

#deel4
def find_password(files_list):
    for file in files_list:
        with open(file) as f:
            content = f.read().lower().splitlines()
            for line in content:
                if 'password' in line:
                    password = line.split(': ')[1]
                    os.chdir(main_path)  
                    return password

    print('password not found')

