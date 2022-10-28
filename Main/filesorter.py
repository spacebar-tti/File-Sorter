from ast import Pass
from genericpath import isdir
from operator import contains
import os
import shutil
import json
import time


descript = 'description'
extension_files = open('file-extensions.json', 'r')
extension_data = json.load(extension_files)
keys = list(extension_data.keys())

# main sorting function
def sort(directory):
    file_pp = str
    all_files = os.listdir(directory)

    for file in all_files:
        file_name = os.path.basename(file)
        file_path = os.path.join(directory, file_name)
        file_path_split = os.path.splitext(file)
        file_ext = file_path_split[-1]

        for key in keys:
            
            if key == file_ext.upper():
                decr_1 = extension_data[key]
                dictname = decr_1[descript]

                new_path = os.path.join(directory, dictname)
                try:
                    os.mkdir(new_path)
                    shutil.move(file_path, new_path)
                except FileExistsError:
                    shutil.move(file_path, new_path)


