from functools import reduce
from math import sqrt
from numbers import Number
from operator import eq, add, sub, mul, and_
from typing import Callable, Any
from collections import Iterable


class Vector:
    """
    Simple vector class
    """
    def __init__(self, *args):
        # in case tuple or list is passed
        if len(args) == 1 and isinstance(args[0], Iterable):
            self.coords = tuple(args[0])
        else:
            self.coords = args

    def __repr__(self):
        return f'Vector{self.coords}'

    def __eq__(self, other):
        return reduce(and_, self._compute_elementwise(other, eq).coords)

    def __getitem__(self, key):
        return Vector(self.coords[key])

    def __len__(self):
        """
        This returns size of the vector not length
        """
        return len(self.coords)

    def __add__(self, other: 'Vector'):
        return self._compute_elementwise(other, add)

    def __sub__(self, other: 'Vector'):
        return self._compute_elementwise(other, sub)

    def __mul__(self, other: Number) -> 'Vector':
        return Vector(*(vi * other for vi in self.coords))

    def __rmul__(self, other: Number) -> 'Vector':
        return Vector(*(vi * other for vi in self.coords))

    def dot(self, other: 'Vector') -> Number:
        multiplied = self._compute_elementwise(other, mul)
        return sum(multiplied.coords)

    def magnitude(self) -> Number:
        return sqrt(self.dot(self))

    def _compute_elementwise(self, other: 'Vector',
                             operator: Callable[[Any, Any], Any]) -> 'Vector':
        """
        Loops through the components of 2 vectors
        and applies given binary operator elementwise

        Input vectors must have the same size
        """
        if len(self) == len(other):
            return Vector(*map(operator, self.coords, other.coords))
        else:
            raise ValueError('Length of vectors must be the same')
