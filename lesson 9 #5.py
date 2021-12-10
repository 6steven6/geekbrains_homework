class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Рисуем ручкой'


class Pencil(Stationery):
    def draw(self):
        return f'Рисуем карандашом'

class Handle(Stationery):
    def draw(self):
        return f'Рисуем маркером'


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
print(pen.draw(), pencil.draw(), handle.draw())
