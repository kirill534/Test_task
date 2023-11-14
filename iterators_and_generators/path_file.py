# Реализуйте функцию gen_files_path,
# которая рекурсивно проходит по всем каталогам указанной директории
# (по умолчанию — корневой диск),
# находит указанный пользователем каталог
# и генерирует пути всех встреченных файлов.
# В решении не нужно использовать рекурсию.
import os
from collections.abc import Iterator


def gen_files_path(abs_path: str, folder: str) -> Iterator[str]:
    for root, dirs, files in os.walk(abs_path):
        for file in files:
            yield os.path.join(root, file)
        if root.endswith(folder):
            print(f'Директория {folder} найдена {root}')
            return


user_folder = input('Пожалуйста, введите название каталога: ')
abs_path = os.path.abspath(os.path.join('..', '..'))
for path_file in gen_files_path('D:/Tasks', user_folder):
    print(path_file)
