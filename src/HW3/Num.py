class Num:

    def __init__(self, at=0, txt=''):
        self.at = at
        self.txt = txt
        self.n, self.mu, self.m2 = 0,0,0
        self.lo, self.hi = float('inf'), float('-inf')
        self.w = -1 if '-$' in self.txt else 1 

    def add(self,n):
        if n != '?':
            self.n+=1
            d = n - self.mu
            self.mu += d/self.n
            self.m2 += d*(n - self.mu)
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)

    def mid(self,x):
        return self.mu

    def div(self,x):
        return (self.m2 <0 or self.n < 2) and 0 or (self.m2/(self.n-1))**0.5

    def rnd(self,x,n):
        return x=='?' and x or self.rnd(x,n)
