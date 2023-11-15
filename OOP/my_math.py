# Реализуйте класс MyMath, состоящий как минимум
# из следующих методов (можете бонусом добавить и другие методы):
#
# вычисление длины окружности,
# вычисление площади окружности,
# вычисление объёма куба,
# вычисление площади поверхности сферы.
# Пример основного кода:
#
# res_1 = MyMath.circle_len(radius=5)
# res_2 = MyMath.circle_sq(radius=6)
# print(res_1)
# print(res_2)
# Результат:
#
# 31.41592653589793
#
# 113.09733552923255
import math


class MyMath:
    @staticmethod
    def circle_len(radius: int) -> float:
        return 2 * math.pi * radius

    @staticmethod
    def circle_sq(radius: int) -> float:
        return math.pi * radius ** 2

    @staticmethod
    def cube_volume(side: int) -> float:
        return side ** 3

    @staticmethod
    def sphere_sq(radius: int) -> float:
        return 4 * math.pi * radius ** 2


res_1 = MyMath.circle_len(radius=5)
print('Вычисление длины окружности:', res_1)
res_2 = MyMath.circle_sq(radius=6)
print('\nВычисление площади окружности:', res_2)
res_3 = MyMath.cube_volume(side=4)
print('\nВычисление объёма куба:', res_3)
res_4 = MyMath.sphere_sq(radius=3)
print('\nВычисление площади поверхности сферы:', res_4)
