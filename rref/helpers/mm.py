
__all__ = [
    "MatrixMadness"
]

"""
Class for creating and manipulating matrix structures
"""

from random import randrange

# Bring in math and utils functions
from .math_ import *
from .utils_ import *


class MatrixMadness:
    """
    Create a matrix of random values from a given rangeo of integers.
    Includes various related methods.
    """

    def __init__(self, matrix=None):
        self.matrix = matrix
        self.math = MathClass()

    def __repr__(self):
        return "<MatrixMadness class>"

    def __set_basic_measures(self):
        self.len = LEN(self.matrix)
        self.row_len = LEN(self.matrix)
        self.col_len = LEN(self.matrix[0])

    def update_matrix(self, matrix):
        self.matrix = matrix
        self.__set_basic_measures()

    @staticmethod
    def creatrix(n_dimensions=20, random_range=[-5, 20]):
        """
        Create a 2-D matrix of random values.

        Parameter:
            n_dimensions: The count of rows and columns in the matrix.
                Example: n_dimensions = 20 will produce a 20x20 matrix of random values
                Default value is 20.

            random_range: A two-integer list from which the domain of the
                    random integer values will be generated.
        """
        if len(random_range) == 2:
            random_range = sorted(random_range)
            return [[randrange(random_range[0], random_range[1]) for i in RANGE(n_dimensions)] for j in RANGE(n_dimensions)]
        print("Please enter a two integer list for range of random values.")

    def sort_it(self, descending=True):
        """Sort matrix instance inplace."""
        self.update_matrix(
            sorted(self.matrix, key=lambda x: x[0], reverse=descending))

    @staticmethod
    def unravel(iterable):
        """Flatten a 2-D iterable into a list of values."""
        return [i for j in iterable for i in j]

    def transpose(self, matrix):
        """Switch matrix rows for columns."""
        return [[matrix[j][i] for j in RANGE(LEN(matrix))] for i in RANGE(LEN(matrix[0]))]

    def inverse_rows(self, matrix):
        """Returns reverse order of rows in matrix."""
        return matrix[::-1]

    def inverse_columns(self, matrix):
        """Reverse order of values in each column"""
        return [row[::-1] for row in matrix]

    def flip_matrix(self, matrix):
        """Invert matrix. Use again to return matrix to original form."""
        return self.inverse_rows(self.inverse_columns(matrix))

    def quarter_rotate(self, matrix, direction='CW'):
        """
        Rotate a matrix one-quarter (90-degrees) turn.  CW for clockwise and CCW for counterclockwise.
        """
        return self.inverse_rows(self.transpose(matrix)) if direction == 'CCW' else self.inverse_columns(self.transpose(matrix))

    @staticmethod
    def get_row(row_index, matrix):
        """Retrieve row by index."""
        return [matrix[row_index][i] for i, v in ENUM(matrix[0])]

    @staticmethod
    def get_column(column_index, matrix):
        """Retrieve column by index."""
        return [matrix[i][column_index] for i, v in ENUM(matrix)]

    @staticmethod
    def sv_product(scalar, vector):
        """
        Multiply all elements of a vector by a scalar.
        Example:
            self.sv_product(-2, [1,2,3,4,]) -> [-2, -4, -6, -8]
        """
        return [scalar * i for i in vector]

    @staticmethod
    def ROW_SUM(vector1, vector2):
        """
        Add together elements from two iterable objects
        that occupy the same position.
        """
        for i in list(zip(vector1, vector2)):
            yield i[0] + i[1]

    @staticmethod
    def no_negatives(matrix):
        """
        Just like TLC's "No Scrubs," but instead of bustas, we don't want no
        negative values.

        This function seeks to eliminate negative values in leading column of
        a matrix.
        """
        return [[matrix[i][j] * -1 if matrix[i][0] < 0 else matrix[i][j] for j in RANGE(LEN(matrix[0]))] for i in RANGE(LEN(matrix))]

    def round_matrix_values(self, matrix=None, n_places=1, inplace=True):
        if matrix is None:
            matrix = self.matrix

        mtrx = [[self.math.ROUND(matrix[i][j], n_places) for j in RANGE(
            LEN(matrix[0]))] for i in RANGE(LEN(matrix))]
        if inplace:
            self.update_matrix(mtrx)
        else:
            return mtrx

    @staticmethod
    def print_matrix(matrix):
        for i in matrix:
            print(i)

    @staticmethod
    def print_matrix_csv(matrix):
        print('\n'.join([','.join([str(i) for i in matrix[x]])
                         for x in RANGE(LEN(matrix))]))
