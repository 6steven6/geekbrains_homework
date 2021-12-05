class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = _income['wage']
        self._income_bonus = _income['bonus']


class Position(Worker):
    def get_full_name(self):
        full_name = f'Имя: {self.name} Фамилия: {self.surname} Должность: {self.position}'
        return full_name

    def get_total_income(self):
        total_income = self._income_wage + self._income_bonus
        return f'Доход: {total_income} $'


worker = Position('steven, ', 'naumkin, ', 'programmer, ', {'wage': 50, 'bonus': 30})

print(worker.get_full_name(), worker.get_total_income())