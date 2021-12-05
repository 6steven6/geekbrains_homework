class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        mass = self._length * self._width * 25 * 5
        return mass


result = Road(10, 10)
print(result.asphalt_mass(), 'тонн')

