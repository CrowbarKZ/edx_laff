from math import isclose
from numbers import Number
from typing import TypeVar


# Any of linear algebra types
LA_ANY = TypeVar('LA_ANY', Number, 'Matrix', 'Vector')


def close_enough(a: LA_ANY, b: LA_ANY) -> bool:
    """
    Tests if the values of operands are 'close enough',
    for testing purposes
    """
    if isinstance(a, Number) and isinstance(b, Number):
        return isclose(a, b)
    elif hasattr(a, '_isclose'):
        return a._isclose(b)
    elif hasattr(b, '_isclose'):
        return b._isclose(a)
    else:
        raise TypeError('Unsupported operand type')
