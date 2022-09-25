import numpy as np

class Gaussian():
    def __init__(self,A):
        self.A = A
        self.m = len(A)
        self.n = len(A[0])
    
    def gaussian_LU_wo_pivot(self):
        k = 0
        for k in range(self.m-1):
            self.A[k:self.m, k] = self.A[k:self.m, k]/self.A[k][k]
            self.A[k:self.m, k:self.m] = self.A[k:self.m, k:self.m] - self.A[k:self.m, k].dot(self.A[k, k:self.m])

        L = np.eye(self.m) + np.tril(self.A, -1)
        U = np.triu(self.A)
        return L, U

    def gaussian_LU_w_pivot(self):
        k = 0
        p = np.eye(self.m, self.n)
        for k in range (self.m-1):
            r = max(enumerate(self.A.T[k][k:self.m]), key = lambda x: abs(x[1]))[0]
            q = r + k
            new_p, new_A = p[k], self.A[k]
            p[k], self.A[k] = p[q], self.A[q]
            p[q], self.A[q] = new_p, new_A
            if self.A[k][k] != 0:
                self.A[k:self.m, k] = self.A[k:self.m, k]/self.A[k][k]
                self.A[k:self.m, k:self.n] = self.A[k:self.m, k:self.n] - self.A[k:self.m, k] @ self.A[k, k:self.n]

        L = np.eye(self.m) + np.tril(self.A, -1)
        U = np.triu(self.A)
        return L, U