from collections import Iterable
from functools import reduce
from math import sqrt, isclose
from numbers import Number
from operator import eq, add, sub, mul, and_
from typing import Callable, Any


class Vector:
    """
    Simple vector class
    Stores components as a tuple
    """
    @classmethod
    def zero(cls, size: int) -> 'Vector':
        """
        Returns the zero vector of given size
        """
        return cls(0 for _ in range(size))

    @classmethod
    def basis(cls, index: int, size: int) -> 'Vector':
        """
        Returns the index'th basis vector of given size
        index starts at 0, e.g. basis(0, 2) == (1, 0)
        """
        assert index < size

        components = [0 for _ in range(size)]
        components[index] = 1
        return cls(components)


    def __init__(self, *args):
        """
        Pass Numbers as args to init, or Iterable of Numbers as 1 arg, e.g.
        Vector(1, 2, 3)
        or
        t = [1, 2, 3]; Vector(t)
        """

        # in case tuple or list is passed
        if len(args) == 1 and isinstance(args[0], Iterable):
            self.components = tuple(args[0])
        else:
            self.components = args

    def __repr__(self):
        return f'Vector{self.components}'

    def __eq__(self, other: 'Vector'):
        return self.components == other.components

    def _isclose(self, other: 'Vector') -> bool:
        """
        Returns true if the components of both Vectors are close enough
        """
        def comparator(a, b):
            # we are ok if the numbers differ by less than 1/10000
            return isclose(a, b, rel_tol=0, abs_tol=0.0001)
        return reduce(and_, self._compute_elementwise(other, comparator).components)

    def __getitem__(self, key):
        return Vector(self.components[key])

    def __iter__(self):
        return self.components.__iter__()

    def __len__(self):
        """
        This returns size of the vector not length
        """
        return len(self.components)

    def __add__(self, other: 'Vector'):
        return self._compute_elementwise(other, add)

    def __sub__(self, other: 'Vector'):
        return self._compute_elementwise(other, sub)

    def __mul__(self, other: Number) -> 'Vector':
        if isinstance(other, Number):
            return Vector(vi * other for vi in self.components)
        else:
            return NotImplemented

    def __rmul__(self, other: Number) -> 'Vector':
        return self.__mul__(other)

    def dot(self, other: 'Vector') -> Number:
        multiplied = self._compute_elementwise(other, mul)
        return sum(multiplied.components)

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
            return Vector(map(operator, self.components, other.components))
        else:
            raise ValueError('Length of vectors must be the same')
