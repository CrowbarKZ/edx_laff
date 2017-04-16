from primitives import Vector, Matrix


if __name__ == '__main__':
    x = Vector(1, -2, 3)
    print(x)

    rows = [
        [0, 0, 0],
        [1, 1, 1],
        [2, 2, 2],
        [3, 3, 3],
    ]
    A = Matrix(rows=rows)
    print(A)

    print(A * x)
