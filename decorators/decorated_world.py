import functools
from typing import Callable


def decorator_with_args_for_any_decorator(my_func: Callable) -> Callable:
    def decorator(*args, **kwargs) -> Callable:
        @functools.wraps(my_func)
        def wrapper(func: Callable) -> Callable:
            result = my_func(func, *args, **kwargs)
            return result

        return wrapper

    return decorator


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    @functools.wraps(func)
    def wrapped(my_args, my_kwargs):
        print(f'Переданные арги и кварги в декоратор: {args} {kwargs}')
        result = func(my_args, my_kwargs)
        return result

    return wrapped


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
