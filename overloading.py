class Square:
    def __init__(self, side):
        self.side = side

    def __add__(square1, square2):
        return (square1.side * 4) + (square2.side * 4)

sq1 = Square(5)
sq2 = Square(10)
print(sq1 + sq2)