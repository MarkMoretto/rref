
__all__ = [
    "MathClass"
]

"""
Class to handle some basic mathematical functions.
"""

from .utils_ import (
    LEN, SUM, RANGE
)


class MathClass:
    """
        Matrix-related math functions
        Includes:
            CEIL: Round value to next higher number
            FLOOR: Round value to next lower number
            ROUND: Round number to a given decimal place
            ROUNDUP: Round number up to the nearest decimal place
            ROUNDUP: Round number down to the nearest decimal place
    """
    @staticmethod
    def CEIL(n):
        return n + (1 - (n % 1))

    @staticmethod
    def FLOOR(n):
        return n - (n % 1)

    def ROUND(self, float_value, n_of_digits=None):
        """Rounding function. Works with floating point values."""
        if n_of_digits is None:
            n_of_digits = 0

        factor = (10 ** n_of_digits)

        if SUM([float_value % 1 for i in RANGE(n_of_digits)]) == 0:
            res = float_value
        else:
            res = self.CEIL(float_value * factor) / factor
        return res

    def __decimal_len(self, n):
        """Find length of decimals."""
        return LEN(str(n)) - LEN(str(n).split('.')[0]) - 1

    def __factor(self, n):
        """Divisor multiple for rounding methods."""
        return 10 ** (n - 1)

    def ROUNDUP(self, float_value):
        """Round up to nearest decimal place"""
        dec_len = self.__decimal_len(float_value)
        factor = self.__factor(dec_len)
        return (int(float_value * factor) + 1) / factor

    def ROUNDDOWN(self, float_value):
        """Round down to nearest decimal place"""
        dec_len = self.__decimal_len(float_value)
        factor = self.__factor(dec_len)
        return int(float_value * factor) / factor
