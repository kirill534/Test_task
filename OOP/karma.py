# Один буддист-программист решил создать свой симулятор жизни,
# в котором нужно набрать 500 очков кармы (это константа), чтобы достичь просветления.
#
# Каждый день вызывается специальная функция one_day(),
# которая возвращает количество кармы от 1 до 7 и может с вероятностью 1 к 10 выкинуть одно из исключений:
#
# KillError,
# DrunkError,
# CarCrashError,
# GluttonyError,
# DepressionError.
# (Исключения нужно создать самостоятельно, при помощи наследования от Exception.)
#
# Напишите такую программу.
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении кармы до уровня константы.
# Исключения обработайте и запишите в отдельный лог karma.log.
#
# По итогу у вас может быть примерно такая структура программы:
#
# открываем файл
#
# цикл по набору кармы
#
#    try
#
#       карма += one_day()
#
#    except(ы) с указанием классов исключений, которые нужно поймать
#
#       добавляем запись в файл
#
# закрываем файл

import random


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day():
    karma = random.randint(1, 7)
    if random.randint(1, 10) == 1:
        error = random.choice([KillError('Умер'), DrunkError('Напился'), CarCrashError('Разбился'),
                               GluttonyError('Объелся'), DepressionError('Депрессия')
                               ])
        raise error

    return karma


with open("karma.log", 'a', encoding='UTF-8') as log_file:
    karma = 0
    day = 0
    while karma < 500:
        day += 1
        try:
            karma += one_day()
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as exc:
            log_file.write(f"День {day}. Проступок {exc}\n")
            if exc.__class__.__name__ == 'KillError':
                print("Вы умерли")
                break

print(f"Вы достигли просветления - {karma} за {day} ")
