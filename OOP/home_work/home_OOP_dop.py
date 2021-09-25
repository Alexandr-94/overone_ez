class Car:
    def __init__(self):
        self.color = color
        self.type_car = type_car
        self.year = year
    def func_z(self):
        print('Автомобиль заведен')
    def func_vk(self):
        print('Автомобиль заглушен')
    def func_year(self):
        print('Год машины',self.year)
    def func_type(self):
        print(self.type_car)
    def func_color(self):

        print(self.color)
car = Car
year = input('введите год автомобиля')
type_car = input('Введите тип автомобиля')
color = input('введите цвет автомобиля')

car.func_z()
