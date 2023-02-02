
# function SYM.new(i,at,txt) --> SYM; constructor
#   i.at, i.txt = at or 0, txt or "" -- col position and name
#   i.n   = 0
#   i.has = {}
#   i.most, i.mode = 0,nil end

# function SYM.add(i,x) --> nil;  update counts of things seen so far
#   if x ~= "?" then 
#    i.n = i.n + 1 
#    i.has[x] = 1 + (i.has[x] or 0)
#    if i.has[x] > i.most then
#      i.most,i.mode = i.has[x], x end end end 

# function SYM.mid(i,x) return i.mode end --> n; return the mode

# function SYM.div(i,x,    fun,e) --> n; return the entropy
#   function fun(p) return p*math.log(p,2) end
#   e=0; for _,n in pairs(i.has) do e = e + fun(n/i.n) end 
#   return -e end

# function SYM.rnd(i,x,n) return x end --> s; return `n` unchanged (SYMs do not get rounded)

# function SYM.dist(i,s1,s2)
#   return s1=="?" and s2=="?" and 1 or (s1==s2) and 0 or 1 end


import math

class Sym:

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

    def dist(self, s1, s2):
        if s1 == "?" and s2 == "?":
            return 1
        if s1 == s2:
            return 0
        else:
            return 1