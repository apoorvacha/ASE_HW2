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
            if x in self.has:
                self.has[x] = self.has[x] + 1
            else: 
                self.has[x] =1 
           
            if self.has[x] > self.most:
                self.most,self.mode = self.has[x],x

    def mid(self,x):
        return self.mode

    def div(self,x):
        def fun(p):
            return p*math.log(p,2)
        e = 0
        for n in self.has:
            p = self.has[n] / self.n
            e += fun(p)
        return -e


    def rnd(self,i,x,n):
        return x
