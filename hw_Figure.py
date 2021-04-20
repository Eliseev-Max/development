#-*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import math

class Figure(metaclass=ABCMeta):
    """Базовый абстрактный класс для фигур: треугольник, прямоугольник, квадрат и круг
    абстрактный метод класса area() - вычисляет площадь фигуры
    абстрактный метод класса perimeter() - вычисляет периметр (длину окружности) фигуры
    метод add_area(Объект_фигуры) - складывает площади текущей и переданной в качестве аргумента фигуры"""
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def add_area(self, figure):
        assert isinstance(figure, Figure),"Передан неверный класс"
        return self.area() + figure.area()

    

class Triangle(Figure):
    __name = "Треугольник"
    __angles = 3
    def __init__(self, side_a, side_b, side_c):
        try:
            assert (side_a + side_b)>side_c, "Треугольника с заданными сторонами не существует"
            assert (side_c + side_b)>side_a, "Треугольника с заданными сторонами не существует"
            assert (side_a + side_c)>side_b, "Треугольника с заданными сторонами не существует"
        except AssertionError as err:
            print(err)
        self.a = side_a
        self.b = side_b
        self.c = side_c
        self.P = self.a + self.b + self.c
        self.__half_P = self.P/2

    @property
    def name(self):
        return self.__name

    @property
    def angles(self):
        return self.__angles
    def area(self):
        return math.sqrt(self.__half_P*(self.__half_P-self.a)*(self.__half_P-self.b)*(self.__half_P-self.c))
    def perimeter(self):
        return self.P

class Rectangle(Figure):
    __name = "Прямоугольник"
    __angles = 4
    def __init__(self, side_a, side_b):
        self.a = side_a
        self.b = side_b
    @property
    def name(self):
        return self.__name
    @property
    def angles(self):
        return self.__angles
    def area(self):
        return self.a*self.b
    def perimeter(self):
        return 2*(self.a + self.b)

class Square(Figure):
    __name = "Квадрат"
    __angles = 4
    def __init__(self, side):
        self.side = side

    @property
    def name(self):
        return self.__name

    @property
    def angles(self):
        return self.__angles
    def area(self):
        return pow(self.side, 2)
    def perimeter(self):
        return 4*self.side

class Circle(Figure):
    __name = "Круг"
    __angles = 0
    def __init__(self, radius):
        self.radius = radius
    @property
    def name(self):
        return self.__name
    @property
    def angles(self):
        return self.__angles
    def area(self):
        #return math.pi*pow(self.radius, 2)
        return 3.14*pow(self.radius, 2)
    def perimeter(self):
        #return 2*math.pi*self.radius
        return round(2*3.14*self.radius)

class Rhombus():
    def __init__(self,diagonal_1, diagonal_2):
        self.d1 = diagonal_1
        self.d2 = diagonal_2
    def area(self):
        return 0.5*self.d1*self.d2

if __name__ == "__main__":
#    base = Figure()        - Нельзя создать инстанс (экземпляр класса) от абстрактного класса
    tr = Triangle(3,4,5)
    re = Rectangle(6,8)
    sq = Square(4)
    ci = Circle(5)
    rh = Rhombus(12,8)
    print(f"Фигура - {tr.name}.\nКоличество углов: {tr.angles}\nПериметр: {tr.perimeter()}\nПлощадь: {tr.area()}")
    print(f"Фигура - {re.name}.\nКоличество углов: {re.angles}\nПериметр: {re.perimeter()}\nПлощадь: {re.area()}")
    print(f"Фигура - {sq.name}.\nКоличество углов: {sq.angles}\nПериметр: {sq.perimeter()}\nПлощадь: {sq.area()}")
    print(f"Фигура - {ci.name}.\nКоличество углов: {ci.angles}\nПериметр: {ci.perimeter()}\nПлощадь: {ci.area()}")
    print(f"Сумма площадей треугольника и прямоугольника: {tr.add_area(re)}\nКвадрата и круга: {sq.add_area(ci)}")
#    print(f"Сумма квадрата и ромба: {sq.add_area(rh)}")     # Возбудит исключение AssertionError, класс Rhombus не наследуется от класса Figure
