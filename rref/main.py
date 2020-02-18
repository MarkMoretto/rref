
__all__ = [
    "RREF",
]


from .helpers import MatrixMadness, RANGE, ENUM


# Abstract base exception class
class ExceptionalException(Exception):
    pass

# Abstracct exception class that extends our base exception


class WheresTheMatrix(ExceptionalException):
    pass


class RREF:
    """
    Row-reduced echelon form class.
    Usage:
        In [0]: rref = RREF(<matrix object>)
        In [1]: rref.run()
        ## Print results to console:
        In [3]: rref.mm.print_matrix(rref.mm.matrix)

        ### Or, without all the fluff:
        In [4]: rref.mm.print_matrix_csv(rref.mm.matrix)
    """

    def __init__(self, matrix_object):
        self.mm = MatrixMadness(matrix_object)

    def __repr__(self):
        return "<RREF class>"

    def __step1(self):
        """
        Step 1: Traverse matrix and set lower-triangle values to zero.
        This is accomplished by:
            1. Dividing a target value by a "base" value
            2. Multiplying that result by -1
            3. Adjusting the base row by that new value
            4. Adding the base row to our target row
        """
        # Eliminate negative values from first column
        self.mm.matrix = self.mm.no_negatives(self.mm.matrix)

        # Iterate matrix, skipping first row
        for r in RANGE(1, self.mm.row_len):
            for c in RANGE(self.mm.col_len):

                # Target coordinates having column numbers smaller than a row numbers
                # This is done to keep focus on "lower-triangle" of matrix
                if c < r:

                    # Set variable to value from first row
                    base_value = self.mm.matrix[r-1][r-1]

                    # If that value is zero, move to the next value.
                    if base_value == 0:
                        base_value = self.mm.matrix[r-1][r]

                    # Target value is the current row-column value
                    # We want to set this value to zero
                    target_value = self.mm.matrix[r][c]

                    # If the value is already zero, we skip it.
                    if target_value != 0:

                        # Set a factor to our target value divided by our base
                        # value and multiply the result by -1.
                        factor = (target_value / base_value) * -1

                        # Adjust our base row by the factor
                        # This utilizes the sv_product(scalar, vector) method from
                        # the MatrixMadness class.
                        adj_base_row = self.mm.sv_product(
                            factor, self.mm.matrix[r-1])

                        # Enumerate our adjusted row and if the column value lines-up
                        # with the target column value, set that to zero.  Otherwise
                        # set the value to the value of the row and the value  of
                        # the adjusted row value in the same location
                        for k, ele in ENUM(adj_base_row):
                            if k == c:
                                self.mm.matrix[r][k] = 0.0
                            else:
                                self.mm.matrix[r][k] += ele

    def __step2(self):
        """
        Step 2: Set the leading value in each row to 1.
        This is done by:
            1. Traversing the matrix from top-to-bottom, left-to-right
            2. Finding the firs nonzero value
            $. Dividing the rest of the row by that value
        """

        # Run through each row of the matrix
        for r in RANGE(self.mm.row_len):

            # We only want the first value, so we have a count variable to act
            # as a constraint
            count = 0

            # For each element of the current row
            for i in self.mm.matrix[r]:

                # If we haven't found a nonzero value yet
                if count < 1:

                    # If the current value isn't zero
                    if i != 0:

                        # Set our divisor variable to the current value
                        divisor = i

                        # Increment our count variable by 1, meeting
                        # the current constraint and moving us to the next phase
                        count += 1

            # Iterate through each column of the matrix
            for c in RANGE(self.mm.col_len):

                # If the current value is not zero
                if not self.mm.matrix[r][c] == 0:

                    # Divide that value by our divisor variable
                    self.mm.matrix[r][c] /= divisor

    def __step3(self):
        """
        Step 3: Finalize matrix into reduced format.  This means to find the 
        first 1 in each row and ensure that any values above that 1 in the same
        column are zero values.  The would make the 1 the only nonzero value in
        that entire column.

        Note that this doesn't apply to other values of 1 in the same row.
        This is accomplished by:
            1. Flipping the entire matrix for easier processing
            2. Finding the first value of 1 in each row
            3. Setting that row as a "base" row
            4. Moving down each subsequent row
            5. Creating a variable from the next value in a column
            6. Adjusting the base row by the opposite sign of that value
            7. Adding the elements from the adjusted base row to the current row
        """
        # 'Flip' the matrix by inverting rows and columns
        # We use the flip_matrix() method from the MatrixMadness class
        self.mm.matrix = self.mm.flip_matrix(self.mm.matrix)

        # Run through all rows except the last one (which will be the 'top' row
        # when the matrix is flipped back into place)
        for r in RANGE(self.mm.row_len - 1):
            for c in RANGE(self.mm.col_len):

                # Find the last 1 in a row by checking to see if the next value
                # is a zero. Because of how the elimination process works, it is
                # unlikely that there will be another 1, 0 combination in subseuqnet
                # rows once initial division has taken place.
                if self.mm.matrix[r][c] == 1 and self.mm.matrix[r][c+1] == 0:

                    # Set our base row to the current row.
                    base_row = self.mm.matrix[r]
                    # Traverse the matrix, but offset the first row by 1 place
                    # to align subsequent values
                    for j in RANGE(r + 1, self.mm.row_len):

                        # We're in the same column as our target 1.  If that
                        # value is already zero, we'll skip it
                        if self.mm.matrix[j][c] != 0:

                            # If it is not zero, set a variable to the negative
                            # value of the current value
                            factor = self.mm.matrix[j][c] * -1

                            # Multiply that variable across our base row
                            adj_base_row = self.mm.sv_product(factor, base_row)

                            # Update each nonzero element of our current row by
                            # adding elements of the adjusted row.  Because the
                            # target value of our base row is 1, it takes the
                            # opposite value of our target and, consequently,
                            # sets that value to zero
                            for k, ele in ENUM(adj_base_row):
                                if ele != 0:
                                    self.mm.matrix[j][k] += ele

    def run(self):
        """"
        Run the whole shebang.
        The resulting matrix will occupy the `self.rref.mm.matrix` variable.
        Results are also rounded onec all calculations are ccomplete.  We're
        only going to 1 decimal place, but that can be adjusted by the user.
        """
        while True:
            self.mm.sort_it()  # Sort matrix from largest to smallest value.
            self.__step1()
            self.__step2()
            self.__step3()
            break
        self.mm.matrix = self.mm.flip_matrix(self.mm.matrix)
        self.mm.round_matrix_values()
