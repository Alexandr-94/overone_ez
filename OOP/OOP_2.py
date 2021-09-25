class Car:
    # статические поля(переменные класса)
    default_color = 'Grey'
    default_weight = 5000

    def __init__(self, color, model):
        # динамические поля(переменные, обьект)
        self.color = color
        self.model = model