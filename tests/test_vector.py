import random
from math import sqrt
from operator import add, sub, mul

from primitives import Vector
from operations.vector import axpy, linear_combination


# init values, we use random values because the code should work
# for all vector lengths / all kinds of float values

vector_size = 10
a_coords = tuple(random.uniform(-100, 100) for _ in range(vector_size))
b_coords = tuple(random.uniform(-100, 100) for _ in range(vector_size))

a = Vector(*a_coords)
b = Vector(*b_coords)

scalar = random.uniform(-100, 100)


def test_creation():
    assert Vector(1) == Vector((1,)) == Vector([1])
    assert Vector(1, 2, 3) == Vector((1, 2, 3)) == Vector([1, 2, 3])


def test_getting_subvector():
    assert a[1] == Vector(a.coords[1])
    assert a[2:5] == Vector(*a.coords[2:5])
    assert a[-4] == Vector(a.coords[-4])


def test_addition():
    assert a + b == Vector(*map(add, a_coords, b_coords))


def test_subtraction():
    assert a - b == Vector(*map(sub, a_coords, b_coords))


def test_multiplication():
    assert a * scalar == Vector(*(ai * scalar for ai in a.coords))


def test_equality():
    assert a == a
    assert a != a * 2


def test_size():
    assert len(a) == len(a.coords)


def test_dot():
    assert a.dot(b) == sum(map(mul, a_coords, b_coords))

    # assert almost equal due to float precision loss sometimes
    # https://docs.python.org/3.6/tutorial/floatingpoint.html
    assert abs(a.dot(b) - (a[:4].dot(b[:4]) + a[4:].dot(b[4:]))) < 0.000000001

def test_axpy():
    assert axpy(scalar, a, b) == a * scalar + b

    # check if axpy'ing partioned vectors fetches the same result
    a1 = a[:4]
    a2 = a[4:]
    b1 = b[:4]
    b2 = b[4:]

    c = axpy(scalar, a, b)
    c1 = axpy(scalar, a1, b1)
    c2 = axpy(scalar, a2, b2)

    assert c[:4] == c1
    assert c[4:] == c2


def test_linear_combination():
    assert linear_combination(a, scalar, b, scalar) == a * scalar + b * scalar


def test_magnitude():
    assert a.magnitude() == sqrt(sum(map(mul, a_coords, a_coords)))






