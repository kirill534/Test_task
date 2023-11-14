# Реализуйте декоратор logging, который будет отвечать
# за логирование функций. На экран выводится название функции и
# её документация. Если во время выполнения декорируемой функции
# возникла ошибка, то в файл function_errors.log
# записываются название функции и ошибки.
#
# Также постарайтесь сделать так, чтобы программа не
# завершалась после обнаружения первой же ошибки,
# а обрабатывала все декорируемые функции и сразу записывала все ошибки в файл.
#
# Дополнительно: запишите дату и время возникновения
# ошибки, используя модуль datetime.
from datetime import datetime
import functools
from typing import Callable


def logging(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        try:
            print(f'Название функции {func.__name__} и документация \n'
                  f'{func.__doc__}')
            func(*args, **kwargs)
        except Exception as exc:
            with open('function_errors.log', 'a', encoding='UTF-8') as log_file:
                log_file.write(f'{datetime.now()} - Название функции {func.__name__}. Ошибка {exc}\n')
    return wrapped_func


@logging
def my_func1() -> None:
    """
    Вывод строки
    """
    print('Hello')


@logging
def my_func2(num: int) -> float:
    """
    Деление на ноль
    """
    return num / 0


@logging
def my_func3() -> str:
    """
    Объединение строки с числом
    """
    return 'I am' + 2 + 'years old'


my_func1()
my_func2(5)
my_func3()

