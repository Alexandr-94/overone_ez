class Human():
    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Name - {self.name}')
        print(f'Age - {self.age}')
        print(f'Money - {self.__money}')
        print(f'House - {self.__house}')

    @staticmethod
    def default_info():
        print(Human.default_name)
        print(Human.default_age)

    def earn_money(self, a):
        self.__money += a

    # Приватный метод
    def __make_deal(self, house, price):
        self.__house = house
        self.__money -= price
    def buy_house(self, house, discount):
                    # Вызываем функцию класса House, т.к. house его объект
        final_price = house.final_price(discount)
        if self.__money < final_price:
            print('fck you')
        else:
            # Выполняем приватный метод, передаём объект и итоговую цену
            self.__make_deal(house, final_price)



class House():
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price - (self._price * (discount / 100))


class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


if __name__ == '__main__':
    Human.default_info()
    alexander = Human('Alexander', 35)
    alexander.earn_money(10000)
    alexander.info()
    drozd = SmallHouse(10000)
    alexander.buy_house(drozd, 10)
    alexander.info()
