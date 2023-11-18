# # Реализуйте класс MyMath, состоящий как минимум
# # из следующих методов (можете бонусом добавить и другие методы):
# #
# # вычисление длины окружности,
# # вычисление площади окружности,
# # вычисление объёма куба,
# # вычисление площади поверхности сферы.
# # Пример основного кода:
# #
# # res_1 = MyMath.circle_len(radius=5)
# # res_2 = MyMath.circle_sq(radius=6)
# # print(res_1)
# # print(res_2)
# # Результат:
# #
# # 31.41592653589793
# #
# # 113.09733552923255
# import math
#
#
# class MyMath:
#     @staticmethod
#     def circle_len(radius: int) -> float:
#         return 2 * math.pi * radius
#
#     @staticmethod
#     def circle_sq(radius: int) -> float:
#         return math.pi * radius ** 2
#
#     @staticmethod
#     def cube_volume(side: int) -> float:
#         return side ** 3
#
#     @staticmethod
#     def sphere_sq(radius: int) -> float:
#         return 4 * math.pi * radius ** 2
#
#
# res_1 = MyMath.circle_len(radius=5)
# print('Вычисление длины окружности:', res_1)
# res_2 = MyMath.circle_sq(radius=6)
# print('\nВычисление площади окружности:', res_2)
# res_3 = MyMath.cube_volume(side=4)
# print('\nВычисление объёма куба:', res_3)
# res_4 = MyMath.sphere_sq(radius=3)
# print('\nВычисление площади поверхности сферы:', res_4)

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_dict = {}

    @property
    def cache(self):
        return next(iter(self.cache_dict)) if self.cache_dict else None

    @cache.setter
    def cache(self, new_elem):
        key, value = new_elem
        if key in self.cache_dict:
            del self.cache_dict[key]
        elif len(self.cache_dict) == self.capacity:
            del self.cache_dict[next(iter(self.cache_dict))]

        self.cache_dict[key] = value

    def print_cache(self):
        print("LRU Cache:")
        for key, value in self.cache_dict.items():
            print(f"{key} : {value}")

    def get(self, key):
        if key in self.cache_dict:
            value = self.cache_dict[key]
            del self.cache_dict[key]
            self.cache_dict[key] = value
            return value
        else:
            return None


# Создаём экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)
# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")
# Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3
# Получаем значение по ключу
print(cache.get("key2"))  # value2
# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")
# Выводим обновлённый кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4