# Пользователь вводит число N. Напишите программу,
# которая генерирует последовательность из
# квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так далее).
# Реализацию напишите тремя способами: класс-итератор,
# функция-генератор и генераторное выражение.

# класс-итератор
print('класс-итератор')
class SquaresIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter ** 2
        raise StopIteration

    def __iter__(self):
        return self


n1 = int(input("Введите число N: "))
iterator = SquaresIterator(n1)
for square in iterator:
    print(square)

print('\nфункция-генератор')


# функция-генератор
def square_generator(limit):
    for square in range(1, limit + 1):
        yield square ** 2


n2 = int(input("Введите число N: "))
generator = square_generator(n2)
for num in generator:
    print(num)

print('\nгенераторное выражение')

# генераторное выражение
n3 = int(input("Введите число N: "))
squares = (num ** 2 for num in range(1, n3 + 1))
for square in squares:
    print(square)
