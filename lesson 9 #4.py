class Car:
    def __init__(self, speed, colour, name, is_police):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police
        self.speed = speed

    def show_speed(self):
        return f'катим со скоростью {self.speed}'

    def go(self):
        return f'едем'

    def stop(self):
        return f'стоим'

    def turn(self, direction):
        return f'поварачиваем на {direction}'


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('ПРЕВЫШЕНИЕ СКОРОСТИ!!!!!!!!!')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('ПРЕВЫШЕНИЕ СКОРОСТИ!!!!!!!!!')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def is_police(self):
        super().is_police()
        is_police = True
        return is_police


car = Car(59, 'red', 'McLaren', True)

print(car.name, car.show_speed(), car.turn('направо'), car.is_police)
