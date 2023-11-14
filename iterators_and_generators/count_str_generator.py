# Реализуйте функцию-генератор, которая берёт все
# питоновские файлы в директории и вычисляет количество
# строк в каждом файле, игнорируя пустые строки и строки комментариев.
# По итогу функция-генератор должна с помощью yield каждый раз
# возвращать количество строк в очередном файле.

import os
from collections.abc import Iterator


def quantity_lines(abs_path: str) -> Iterator[str]:
    for dirpath, dirname, filenames in os.walk(abs_path):
        if 'venv' in dirname:
            dirname.remove('venv')
        for file_name in filenames:
            all_quantity = 0
            if file_name.endswith('.py'):
                with open(os.path.join(dirpath, file_name), 'r', encoding='UTF-8') as file_py:
                    for line in file_py:
                        if line == '\n' or line.startswith(('#', '"', "'")):
                            continue
                        else:
                            all_quantity += 1
                    yield os.path.join(dirpath, file_name), all_quantity


abs_path = os.path.abspath(os.path.join('..'))
path_file_py = list(quantity_lines(abs_path))

for path_file in path_file_py:
    print(f'Файл {path_file[0]} имеет строк кода: {path_file[1]}')
