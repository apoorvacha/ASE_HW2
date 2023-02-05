import math 
class Num:
    def __init__(self, n =0, mu =0, m2=0):
        self.n = n
        self.mu = mu
        self.m2 = m2
        self.lo = float('inf')
        self.hi = float('-inf')


    def add(self, n):
        if n !="?":
            self.n = self.n + 1
            d = n - self.mu
            self.mu = self.mu + (d / self.n)
            self.m2 = self.m2 + (d * (n - self.mu))
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)


    def mid(self):
        return self.mu # n; return mean

    #n; return standard deviation using Welford's algorithm 
    def div(self): 
        if self.m2 < 0 or self.n < 2:
            return 0
        else:
            return pow((self.m2/(self.n-1)),0.5)