'''Задание 4 (архивация):
Создай программу, которая:
Архивирует все .txt файлы из текущей директории в backup.zip.'''

from zipfile import ZipFile
import os

with ZipFile('backup.zip', 'w') as zipfile:
    for file in os.listdir('.'):
        if os.path.isfile(file):
            if file.endswith('.txt'):
                zipfile.write(file)
                os.remove(file)


