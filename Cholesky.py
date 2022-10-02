import numpy as np
from cmath import sqrt


class Cholesky():
    def __init__(self, A):
        self.A = A
        self.m = len(A)

    def cholesky_factorization(self):
        k = 0
        for k in range (self.m+1):
            if self.A[k][k] < 0:
                raise Exception('Matrix should be positive definite')
        
            self.A[k][k] = np.sqrt(self.A[k][k])
            self.A[k+1:, k] = self.A[k+1:, k] / self.A[k][k]
            for j in range (k, self.m+1):
                self.A[j:, j] = self.A[j:, j] - self.A[j:, k]@self.A[j, k]
            self.A[k, k+1:self.m+1] = np.zeros(1, self.m-k)
        return self.A