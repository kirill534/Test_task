# В программировании иногда возникает ситуация,
# когда работу функции нужно замедлить.
# Типичный пример — функция, которая постоянно проверяет,
# изменились ли данные на веб-странице или её код.
#
# Реализуйте декоратор, который перед выполнением
# декорируемой функции ждёт несколько секунд.

import math
import time
import functools
from typing import Callable


def time_sleep(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        stared_at = time.time()
        time.sleep(2)
        result = func(*args, **kwargs)
        ended_at = time.time()
        print('Функция работала:', round(ended_at - stared_at, 2))
        return result
    return wrapped_func


@time_sleep
def my_func(number) -> None:
    return round(math.sqrt(sum([i_elem ** 20 for i_elem in range(number)])), 2)


my_func(1000000)
