class Tomato:
    state = {1:'не спелый',
              2:'Почти готов',
              3:'Можно кушать'}
    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._state += 1
        return 'новая стадия'
    def is_ripe(self):
        if self._state == 3:
            print('готов')
        else:
            print('не готов')


# to = Tomato(1)
# print(to)
# print(to.grow())
# print(to._state)
# print(to.grow())
# print(to._state)

class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1,num)]
        self.num = num
    def grow_all(self):
        for i in self.tomatoes:
            i.grow()
            print(i._state)
    def all_are_ripe(self):
        for i in self.tomatoes:
            i.is_ripe()
        return True
    def give_away_all(self):
        self.tomatoes.clear()
        print(self.tomatoes)



to = TomatoBush(6)
# # print(to.tomatoes)
# to.grow_all()
# to.grow_all()
# to.grow_all()
# print(to.all_are_ripe())
# print(to.give_away_all())

class Gardener:
    def __init__(self, name,plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    #
    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
    @staticmethod
    def knowledge():
        print( 'I know something!')



w=TomatoBush(5)
ga = Gardener('Alexandr',w)
ga.work()
ga.work()
ga.work()
ga.harvest()
ga.knowledge()