class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) \
               + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return 'Sum of cell is ' + str(self.nums + other.nums)
        # return Cell(self.nums + other.nums)

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else 'ячеек в первой клетке меньше либо равны второй, вычитание невозможно'

    def __mul__(self, other):
        return 'Multiply of cells is ' + str(self.nums * other.nums)

    def __truediv__(self, other):
        return 'Truediv of cells is ' + str(round(self.nums / other.nums))



