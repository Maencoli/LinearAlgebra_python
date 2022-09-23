import numpy as np

class Gaussian():
    def __init__(self,A):
        self.A = A
        self.m = len(A)
    
    def gaussian_LU (self):
        k = 0
        for k in range(self.m-1):
            self.A[k:self.m, k] = self.A[k:self.m, k]/self.A[k][k]
            self.A[k:self.m, k:self.m] = self.A[k:self.m, k:self.m] - self.A[k:self.m, k] @ self.A[k, k:self.m]

        L = np.eye(self.m) + np.tril(self.A, -1)
        U = np.triu(self.A)
        return L, U
        