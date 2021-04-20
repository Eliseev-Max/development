# -*-coding: utf-8 -*-
from Figures.figures import Figure as Figure
from Figures.figures import Triangle as T
from Figures.figures import Rectangle as R
from Figures.figures import Square as S
from Figures.figures import Circle as C
import pytest

triangle = T(3,4,5)
rectangle = R(8,10)
square = S(4)
circle = C(10)

def test_triangleIsInstance():
    assert isinstance(triangle, Figure),"Класс 'Figure' не является базовым"
def test_rectangleIsInstance():
    assert isinstance(rectangle, Figure),"Класс 'Figure' не является базовым"
def test_squareIsInstance():
    assert isinstance(square, Figure),"Класс 'Figure' не является базовым"
def test_circleIsInstance():
    assert isinstance(circle, Figure),"Класс 'Figure' не является базовым"


def test_triangles_area_counts():
#    triangle = T(3,4,5)
    assert triangle.area() !=0,"Площадь треугольника не может быть равной нулю"
    assert triangle.area() == 6,"Ошибка в вычислении площади"


def test_triangles_perimeter_counts():
#    triangle = T(3,4,5)
    assert triangle.perimeter() !=0,"Периметр треугольника не может быть равен нулю"
    assert triangle.perimeter() == 12,"Ошибка в вычислении преиметра"

#@pytest.mark.skip
def test_is_triangle_exists():
    wrongTriangle = T(3,4,9)


def test_rectangles_area_counts():
    rectangle = R(8,10)
    assert rectangle.area() !=0,"Площадь прямоугольника не может быть равной нулю"
    assert rectangle.area() == 80,"Ошибка в вычислении площади"


def test_rectangles_perimeter_counts():
    rectangle = R(8,10)
    assert rectangle.perimeter() !=0,"Периметр прямоугольника не может быть равен нулю"
    assert rectangle.perimeter() == 36,"Ошибка в вычислении преиметра"

def test_square_area_counts():
    square = S(6)
    assert square.area() !=0,"Площадь квадрата не может быть равной нулю"
    assert square.area() == 36,"Ошибка в вычислении площади"


def test_square_perimeter_counts():
    square = S(6)
    assert square.perimeter() !=0,"Периметр квадрата не может быть равен нулю"
    assert square.perimeter() == 24,"Ошибка в вычислении преиметра"


def test_circle_area_counts():
    circle = C(10)
    assert circle.area() !=0,"Площадь круга не может быть равной нулю"
    assert circle.area() == 314,"Ошибка в вычислении площади"


def test_circumference_counts():
    circle = C(10)
    assert circle.perimeter() !=0,"Длина окружности не может быть равна нулю"
    assert circle.perimeter() == 2*3.14*10,"Ошибка в вычислении длины окружности" 
