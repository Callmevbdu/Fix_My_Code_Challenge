#!/usr/bin/python3

class square():
     
    def __init__(self, length):
        self.length = length

    def area_of_my_square(self):
        """ Area of the square """
        return self.length * self.length

    def PermiterOfMySquare(self):
        return self.length * 4

    def __str__(self):
        return f"Square with length: {self.length}"

if __name__ == "__main__":

    s = square(12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
