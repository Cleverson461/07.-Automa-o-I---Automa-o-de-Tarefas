""" 
    Organizador de Arquivos
    
    1. Nesse exercício vamos colocar em prática o que aprendemos nas aulas anteriores.
    
    2. O seu desafio é criar um programa em Python que organiza arquivos de acordo com so seguintes tipos de arquivos:
    
    -: exe
    -: csv
    -: jpg
    -: pdf
    -: zip
    -: txt
    -: py
    -: xlsx
"""

import os

# 1 - Diretório raiz do OS
base_path = os.path.expanduser('~')
#print(base_path)

# 2 - Navega no diretório Downloads
path = os.path.join(base_path, 'Downloads')
#print(path)
work_dir = os.chdir(path)

# 3 - Lista arquivos do diretório
list_files = os.listdir(work_dir)
#print(list_files)

# 4 - Criar Pastas
type_files = ['exe', 'csv', 'jpg', 'pdf', 'zip', 'txt', 'py', 'xlsx', 'png', 'mp4', 'docx', 'epub', 'rar']
for type in type_files:
    if type not in os.listdir():
        os.mkdir(type)
        
# 5 - Organizando arquivos
for file in list_files:
    for type in type_files:
        if '.' +type in file:
            old_path = os.path.join(path, file)
            new_path = os.path.join(path, type, file)
            os.replace(old_path, new_path)