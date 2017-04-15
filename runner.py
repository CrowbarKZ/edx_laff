from primitives import Vector


if __name__ == '__main__':
    a = Vector(3, 5)
    b = Vector(1, 2)

    print(a, b)
    print(a + b)
    print(a - b)
    print(a * 2)
    print(a == b, a == a)
