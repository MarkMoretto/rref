# Reduced Row-Echelon Form (RREF) library

This is a simple library for transforming a 2-D matrix to reduced row-echelon form (RREF)<sup>[1]</sup>.

Definition<sup>[2]</sup>:

>In linear algebra, a matrix is in echelon form if it has the shape resulting from a Gaussian elimination.

>A matrix being in row echelon form means that Gaussian elimination has operated on the rows, and column echelon form means that Gaussian elimination has operated on the columns. In other words, a matrix is in column echelon form if its transpose is in row echelon form. Therefore, only row echelon forms are considered in the remainder of this article. The similar properties of column echelon form are easily deduced by transposing all the matrices.

A matrix is in reduced row-echelon form if it satisfies the following:
1. In each row, the left-most nonzero entry is 1 and the column that contains this 1 has all other entries equal to 0. This 1 is called a leading 1.
2. The leading 1 in the second row or beyond is to the right of the leading 1 in the row just above.
3. Any row containing only 0's is at the bottom.

Below is a screenshot showing RREF matrices<sup>[3]</sup>:

![RREF examples](/static/rref1.png)

---
## Example Usage
``` python
import rref

### Create an uninstanced matrix helper (MatrixMadness)
mm = rref.main.MatrixMadness()

### Create a sample matrix of 20 x 20 with random integers 
### in the range of -5 to 20.
matrix = mm.creatrix(20, [-5, 20])

### Create an RREF instance with your matrix.
r = rref.RREF(matrix)

### Run the processor
# Note: The output matrix will be in the r.mm.matrix variable.
r.run()

### Print the matrix to check results.
result = r.mm.matrix
print([i for i in result])

```


[1]: https://people.math.carleton.ca/~kcheung/math/notes/MATH1107/wk04/04_reduced_row-echelon_form.html
[2]: https://en.wikipedia.org/wiki/Row_echelon_form
[3]: https://stattrek.com/statistics/dictionary.aspx?definition=reduced_row_echelon_form
