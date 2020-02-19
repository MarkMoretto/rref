import re
import rref
from rref.helpers.utils_ import stoi, string_to_matrix


def string_to_matrix(string_object):
    if len(string_object) == 0:
        print("Invalid string detected.")
    else:
        sso = string_object.strip()
        lines = sso.split("\n")
        out_mtrx = list()
        for line in lines:
            out_mtrx.append([stoi(i) for i in re.split(r"\s+", line)])
        return out_mtrx


sample_1 = """
-7 -6 -12 -33
2  1  1  8
1  1  0  5
"""

exp_res_1 = """
1  0  1  3
0  1 −1  2
0  0  0  0
"""

matrix1 = string_to_matrix(sample_1)
expected2 = string_to_matrix(exp_res_1)


r1 = rref.main.RREF(matrix1)
r1.run()
r1.mm.matrix


sample_2 = """
1 -1 2 1
2  1 1 8
1  1 0 5
"""

exp_res_2 = """
1  0  1  3
0  1 −1  2
0  0  0  0
"""

matrix2 = string_to_matrix(sample_2)
expected2 = string_to_matrix(exp_res_2)

# print(matrix2)

r2 = rref.main.RREF(matrix2)
r2.run()
print(r2.mm.matrix)
