import functools
from collections.abc import Callable


def check_permission(permission: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            try:
                if permission in user_permissions:
                    return func(*args, **kwargs)
                raise PermissionError
            except PermissionError:
                print('PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию', func.__name__)

        return wrapped_func

    return decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
