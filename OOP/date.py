# Реализуйте класс Date, который должен:
#
# проверять числа даты на корректность;
# конвертировать строку даты в объект класса Date,
# состоящий из соответствующих числовых значений дня, месяца и года.
# Оба метода должны получать на вход строку вида ‘dd-mm-yyyy’.
#
# При тестировании программы объект класса
# Date должен инициализироваться исключительно через метод конвертации, например:
#
# date = Date.from_string('10-12-2077')
# Неверный вариант: date = Date(10, 12, 2077)
#
# Пример основного кода:
#
# date = Date.from_string('10-12-2077')
# print(date)
# print(Date.is_date_valid('10-12-2077'))
# print(Date.is_date_valid('40-12-2077'))
# Результат:
# День: 10    Месяц: 12    Год: 2077
# True
# False

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    def __str__(self) -> str:
        return f'День: {self.day}\tМесяц: {self.month}\tГод: {self.year}'

    @classmethod
    def editing_date(cls, date: str) -> None:
        cls.day, cls.month, cls.year = map(int, date.split('-'))

    @classmethod
    def from_string(cls, date) -> 'Date':
        cls.editing_date(date)
        return cls(cls.day, cls.month, cls.year)

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        cls.editing_date(date)
        return 0 < cls.day < 32 and 0 < cls.month < 13 and 2000 < cls.year < 2100


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-1-2077'))
print(Date.is_date_valid('40-12-2077'))
