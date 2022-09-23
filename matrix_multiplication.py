import numpy as np

class MatrixMultiplication():
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.m = len(A)
        self.n = len(np.transpose(B))
        self.p = len(B)

        if len(A) != len(B[0]):
            print('CANNOT CALCULATE AS SIZE A AND B DO NOT MATCH')

    def case_prod(self):
        self.C = np.zeros((self.m, self.n))
        i = j = k = 0
        for j in range(self.n):
            for i in range(self.m):
                for k in range (self.p):
                    self.C[i][j] += self.A[i][k] + self.B[k][j]
        return self.C
    
    def case_dot(self):
        self.C = np.zeros((self.m, self.n))
        i = j = 0
        for j in range(self.n):
            for i in range(self.m):
                self.C[i] = self.A[i] * np.transpose(self.B)[j]

        return self.C
    
    def case_col(self):
        self.C = np.zeros((self.m, self.n))
        j = 0
        for j in range(self.n):
            self.C[j] += self.A * np.transpose(self.B)[j]
    
    def case_row(self):
        self.C = np.zeros((self.m, self.n))
        i = 0
        for i in range(self.m):
            self.C[i] += self.A[i] * self.B
        return self.C
    
    def case_outer(self):
        self.C = np.zeros((self.m, self.n))
        k = 0
        for k in range(self.p):
            self.C += np.transpose(self.A)[k] * self.B[k]
        return self.C
    
    def case_direct(self):
        self.C = np.zeros((self.m, self.n))
        self.C = self.A * self.B
        return self.C