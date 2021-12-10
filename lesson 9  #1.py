from time import sleep
from itertools import cycle


class TrafficLight:

    def __init__(self):
        self.__colour = (('красный', 5), ('желтый', 2), ('зелёный', 3))

    def running(self):
        for colour, sec in cycle(self.__colour):
            print(colour)
            sleep(sec)


trafficlight = TrafficLight()
trafficlight.running()
