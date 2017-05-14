from itertools import chain
from numbers import Number
from typing import Iterable, Tuple

from primitives import Vector


class Matrix:
    """
    Simple matrix class
    Stores components as tuple of tuples (tuple of rows)

    Rounds all component values to certain set decimal digit, for ez testing
    """
    @classmethod
    def zero(cls, m: int, n: int) -> 'Matrix':
        """
        Returns the zero matrix of given dimensions
        """
        return cls(rows=(Vector.zero(n) for _ in range(m)))

    @classmethod
    def identity(cls, m: int) -> 'Matrix':
        """
        Returns the identity matrix m by m
        """
        return cls(rows=(Vector.basis(i, m) for i in range(m)))

    def __init__(self, rows: Iterable[Iterable[Number]] = None,
                 cols: Iterable[Iterable[Number]] = None):
        """
        Expects either rows or cols to be set, not both
        if rows are set, cols will be ignored
        """
        if rows:
            self.components = tuple(tuple(row) for row in rows)
        elif cols:
            rows = zip(*cols)
            self.components = tuple(rows)
        else:
            raise ValueError('Either rows or cols must be set')

    def __repr__(self):
        result = 'Matrix: \n'
        for row in self.components:
            result += repr(row) + '\n'
        return result

    def __getitem__(self, key):
        return self.components[key]

    def __mul__(self, other: Vector):
        return Vector(Vector(row).dot(other) for row in self.components)

    def __rmul__(self, other: Vector):
        return self.__mul__(other)

    def __eq__(self, other: 'Matrix'):
        return self.components == other.components

    def _isclose(self, other: 'Matrix') -> bool:
        """
        Returns true if the components of both Matrices are close enough
        """
        component_results = (
            a.__isclose(b) for a, b
            in zip(self.vectorize_rows, other.vectorize_rows)
        )
        return reduce(and_, component_results)

    def vectorize_rows(self) -> Iterable[Vector]:
        """
        Returns components as iterator where each row is represented by a Vector
        """
        return (Vector(row) for row in self.components)

    def transpose(self) -> 'Matrix':
        """
        Returns a transposed version of self
        """
        return Matrix(cols=self.components)
