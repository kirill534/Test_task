# Реализуйте декоратор counter, считающий и
# выводящий количество вызовов декорируемой функции.
#
# Для решения задачи нельзя использовать операторы global и nonloca
import functools
from typing import Callable


def counter(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        wrapped_func.count += 1
        result = func(*args, **kwargs)
        return result
    wrapped_func.count = 0
    return wrapped_func


@counter
def my_func1():
    pass


@counter
def my_func2():
    pass


my_func1()
my_func1()
my_func1()
my_func2()

print(f'Функция {my_func1.__name__} вызывалась: {my_func1.count} раз/раза')
print(f'Функция {my_func2.__name__} вызывалась: {my_func2.count} раз/раза')
