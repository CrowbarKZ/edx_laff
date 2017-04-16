import random
from primitives import Matrix, Vector

rownum = 10
colnum = 10

rows = [[random.uniform(-100, 100) for i in range(colnum)] for j in range(rownum)]
cols = zip(*rows)

x = Vector(random.uniform(-100, 100) for i in range(colnum))
A = Matrix(rows=rows)


def test_creation():
    rows2 = [
        [0, 0, 0],
        [1, 1, 1],
        [2, 2, 2],
        [3, 3, 3],
    ]
    cols2 = [
        [0, 1, 2, 3],
        [0, 1, 2, 3],
        [0, 1, 2, 3],
    ]
    assert Matrix(rows=rows2) == Matrix(cols=cols2)
    assert Matrix(rows=rows) == Matrix(cols=cols)


def test_getitem():
    assert A[0][0] == rows[0][0]
    assert A[5][5] == rows[5][5]


def test_matrix_vector_multiplication():
    result = []
    for i in range(rownum):
        result.append(Vector(A[i]).dot(x))

    y = Vector(result)
    assert A * x == y
    assert x * A == y
