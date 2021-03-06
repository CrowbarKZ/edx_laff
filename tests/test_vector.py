import random
from math import sqrt
from operator import add, sub, mul

from helpers.comparison import close_enough
from operations.vector import axpy, linear_combination
from primitives import Vector


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


def test_basis_creation():
    assert Vector.basis(0, 2) == Vector(1, 0)
    assert Vector.basis(3, 6) == Vector(0, 0, 0, 1, 0, 0)


def test_zero_creation():
    assert Vector.zero(2) == Vector(0, 0)
    assert Vector.zero(5) == Vector(0, 0, 0, 0, 0)


def test_vector_splitting_to_basis_products():
    product_vector = Vector.zero(len(a))
    for i, component in enumerate(a):
        product_vector += Vector.basis(i, len(a)) * component

    assert product_vector == a


def test_getting_subvector():
    assert a[1] == Vector(a.components[1])
    assert a[2:5] == Vector(*a.components[2:5])
    assert a[-4] == Vector(a.components[-4])


def test_addition():
    assert a + b == Vector(map(add, a_coords, b_coords))
    assert a + b == b + a


def test_subtraction():
    assert a - b == Vector(map(sub, a_coords, b_coords))
    assert a - b == -1 * (b - a)


def test_multiplication():
    assert a * scalar == Vector(ai * scalar for ai in a.components)
    assert scalar * a == Vector(ai * scalar for ai in a.components)


def test_equality():
    assert a == a
    assert a != a * 2


def test_close_enough():
    assert close_enough(a, a)
    assert close_enough(a, a + a * 0.00000000000000000000000000001)
    assert not close_enough(a, a + a * 0.01)


def test_size():
    assert len(a) == len(a.components)


def test_dot():
    assert a.dot(b) == sum(map(mul, a_coords, b_coords))
    assert a.dot(b) == b.dot(a)

    # assert almost equal due to float precision loss sometimes
    # https://docs.python.org/3.6/tutorial/floatingpoint.html
    assert close_enough(a.dot(b), (a[:4].dot(b[:4]) + a[4:].dot(b[4:])))

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






