import functools
import time
from datetime import datetime
from typing import Callable


def timer(cls, func: Callable, date) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        date_form = date
        for i_elem in date_form:
            if i_elem.isalpha():
                date_form = date_form.replace(i_elem, '%' + i_elem)
        print(f"Запускается '{cls.__name__}.{func.__name__}.' "
              f"Дата и время запуска: {datetime.now().strftime(date_form)}.")
        started_at  = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        print(f'Завершение {cls.__name__}.{func.__name__}, время работы =', round(ended_at - started_at, 2))
        return result
    return wrapped_func


def log_methods(date: str) -> Callable:
    def decorator(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                cur_method = getattr(cls, i_method_name)
                decorated_method = timer(cls, cur_method, date)
                setattr(cls, i_method_name, decorated_method)
        return cls

    return decorator


@log_methods("b d Y — H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test_sum_1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Тут метод test_sum_1 у наследника")

    def test_sum_2(self):
        print("Тут метод test_sum_2 у наследника.")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()

# Запускается 'B.test_sum_1'. Дата и время запуска: Apr 23 2021 — 21:50:37.
# Запускается 'A.test_sum_1'. Дата и время запуска: Apr 23 2021 — 21:50:37.
# Тут метод test_sum_1.
# Завершение 'A.test_sum_1', время работы = 0,187 s.
# Тут метод test_sum_1 у наследника.
# Завершение 'B.test_sum_1', время работы = 0,187 s.
# Запускается 'B.test_sum_2'. Дата и время запуска: Apr 23 2021 — 21:50:37.
# Тут метод test_sum_2 у наследника.
# Завершение 'B.test_sum_2', время работы = 0,370 s.
