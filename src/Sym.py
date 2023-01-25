import math

class sym:

    def __init__(self, at=0, txt= ''):
        self.at = at
        self.txt = txt
        self.n = 0
        self.has = {}
        self.most = 0
        self.mode = None

    def add(self,x):
        if x != '?':
            self.n+=1
            self.has = 1 + (self.has[0] if self.has else 0)
            if self.has[x] > self.most:
                self.most,self.mode = self.has[x],x

    def mid(self,x):
        return self.mode

    def div(self,x,e):
        def fun(p):
            return p*math.log(p,2)
        e = 0
        for _,n in self.has:
            e += fun(n/self.n)
        return -e

    def rnd(self,i,x,n):
        return x
