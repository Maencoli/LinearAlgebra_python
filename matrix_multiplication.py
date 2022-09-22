import numpy as np


class MatrixMultiplication():
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.m = len(A)
        self.n = len(B[0])
        self.p = len(A[0])
        self.C = np.zeros((len(A), len(B[0])))

        if len(A) != len(B[0]):
            print('CANNOT CALCULATE AS SIZE A AND B DO NOT MATCH')

    def case_prod(self):
        i = j = k = 0
        for j in range(self.n):
            for i in range(self.m):
                for k in range (self.p):
                    self.c[i][j] = self.c[i][j] + self.A[i][k] + self.B[k][j]
        return self.C
    
    def case_dot(self):
        