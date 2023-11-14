# Создайте декоратор, который кэширует (сохраняет для дальнейшего использования)
# результаты вызова функции и, при повторном вызове
# с теми же аргументами, возвращает сохранённый результат.
#
# Примените его к рекурсивной функции вычисления чисел Фибоначчи.
#
# В итоге декоратор должен проверять аргументы, с которыми
# вызывается функция, и, если такие аргументы уже использовались,
# должен вернуть сохранённый результат вместо запуска расчё
import functools
import time
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_num = {}

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):

        if args in cache_num:
            return cache_num[args]
        else:
            result = func(*args, **kwargs)
            cache_num[args] = result
            return result

    return wrapped_func


@cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(99))
print('-'*20)
print(fibonacci(100))
print('-'*20)
print(fibonacci(50))