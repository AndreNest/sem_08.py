class Car:
    def __init__(self, color, brand):
        self.e_on = False
        self.color = color
        self.brand = brand
    def start_engine(self):
        self.e_on = True
    def drive_to(self, city):
        if self.e_on:
            print(f"Мы едем в {city}, на {self.color} {self.brand}")
        else:
            print('Мы никуда не едем. Заведите двигатель!')

c = Car('красном', 'мерседесе')
c.start_engine()
c.drive_to('Москву')

class Book:
    def __init__(self, name, auth):
        self.name = name
        self.auth = auth
    def get_name(self):
        return self.name
    def get_auth(self):
        return  self.auth

book = Book('Война и мир', 'Л.Толстой')
print(f'Книга - "{book.get_name()}", писатель - {book.get_auth()}')

from math import pi

class Circle:
    def __init__(self, radios):
        self.radios = radios
    def area(self):
        return pi * self.radios ** 2
    def perimeter(self):
        return 2 * pi * self.radios

class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
    def perimeter(self):
        return 4 * self.side

def print_shape_info(shape):
    print(f"Area = {shape.area()}, perimetr = {shape.perimeter()}")
square = Square(10)
print_shape_info(square)

circle = Circle(10)
print_shape_info(circle)


class Time:
    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds
    def __add__(self, other):
        m = self.minutes + other.minutes
        s = self.seconds + other.seconds
        m += s // 60
        s = s % 60
        return Time(m,s)
    def __sub__(self, other):
        m = self.minutes - other.minutes
        s = self.seconds - other.seconds
        m += s // 60
        s = s % 60
        return Time(m,s)
    def info(self):
        return f"{self.minutes}:{self.seconds}"
    def __str__(self):
        return f"{self.minutes}:{self.seconds}"


t1 = Time(5, 50)
print(t1.info())

t2 = Time(3, 30)
print(t2.info())

t3 = t2 + t1

print(t3.info())

print(t1)

t4 = t1 - t2
print(t4)
