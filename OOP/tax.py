# Реализуйте иерархию классов, описывающих имущество налогоплательщиков.
# Она должна состоять из базового класса Property и производных от него классов Apartment, Car и CountryHouse.
#
# Базовый класс должен иметь атрибут worth (стоимость),
# который передаётся в конструктор, и метод расчёта налога,
# переопределённый в каждом из производных классов.
# Налог на квартиру вычисляется как 1/1000 её стоимости, на машину — 1/200, на дачу — 1/500.
#
# Каждый дочерний класс должен иметь конструктор с одним параметром,
# передающий свой параметр конструктору базового класса.
#
# Разработайте интерфейс программы.
# Пусть она запрашивает у пользователя количество его денег и стоимость имущества,
# а затем выдаёт налог на соответствующее имущество и показывает,
# сколько денег ему не хватает (если это так).

class Property():
    def __init__(self, worth):
        self.worth = worth

    def tax_calculation(self):
        pass


class Apartment(Property):
    name = 'Квартира'

    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.worth / 1000


class Car(Property):
    name = 'Машина'

    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.worth / 200


class CountryHouse(Property):
    name = 'Дача'

    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.worth / 500


def main():
    money = float(input('Введите сколько у вас денег: '))
    property_value = float(input('Введите стоимость имущества: '))

    property = [Apartment, Car, CountryHouse]

    total_tax = 0
    for property_type in property:
        property_objects = property_type(property_value)
        tax = property_objects.tax_calculation()
        total_tax += tax

    if total_tax > money:
        shortage = total_tax - money
        print(f'Налог на ваше имущество: {total_tax}\n'
              f'Вам не хватает {shortage} денег')
    else:
        print(f"Налог на ваше имущество: {total_tax}")
        print("У вас достаточно денег")


main()
