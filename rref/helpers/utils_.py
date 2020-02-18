

__all__ = [
    "RANGE",
    "ENUM",
    "SUM",
    "LEN",
    "ABS",
    "cls_property",
]


def RANGE(start, stop=None, increment=None):
    """
    Variation on range() that increments/decrements
    based on variable sign. Auto-sort feature means there
    is no wrong way to enter the first two values.

    Default increment is 1.

    Increment of -1 includes end value:
        RANGE(10, increment=-1) will produce 11 values, ending at zero
        RANGE(10, 1, -1) will produce 10 values, ending at 1.
    """
    if stop is None:
        stop = start
        start = 0

    if increment is None:
        increment = 1

    value_list = sorted([start, stop])
    if increment == 0:
        print('Error! Please enter nonzero increment value!')
    else:
        value_list = sorted([start, stop])
        if increment < 0:
            start = value_list[1]
            stop = value_list[0]
            while start >= stop:
                worker = start
                start += increment
                yield worker
        else:
            start = value_list[0]
            stop = value_list[1]
            while start < stop:
                worker = start
                start += increment
                yield worker


def SUM(iterable):
    """Pass matrix to iter_vals function; increment and return total"""
    totes = 0
    for v in iterable:
        totes += v
    return totes


def LEN(x):
    """Get length (character count) of an object."""
    return int(SUM([1 for i in x]))


def ENUM(iterable, start=0, increment=1):
    """Enumerate an iterable without all the fuss!"""
    n = start
    for i in iterable:
        tmp = n
        n += increment
        yield tmp, i


def ABS(n):
    """Returns absolute value of a number."""
    return n if n >= 0 else n * -1


def cls_property(name, data_type):
    """Helper function to define class properties."""

    masked_name = "__" + name

    @property
    def prop(self):
        return getattr(self, masked_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, data_type):
            raise TypeError(f"Expected data type for {name} is {data_type}.")
        setattr(self, masked_name, value)

    return prop
