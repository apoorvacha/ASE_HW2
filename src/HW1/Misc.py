import math
from Start import the
def rnd(n, nPlaces=3):
    mult = 10**(nPlaces or 3)
    return math.floor(n * mult + 0.5) / mult

# oo, rand , generate, 

def rand(lo=0,hi=1):
    seed1 = the["seed"]
    seed1 = (16807*seed1) % 2147483647
    return lo+(hi-lo) * seed1/2147483647

# def map(t,fun,u): # t; map a function `fun`(v) over list (skip nil results)
#   u={}
#   for k,v in pairs(t):
#     v,k=fun(v); u[k or (1+#u)]=v end;  return u end

# def kap(t, fun,     u): # t; map function `fun`(k,v) over list (skip nil results)
#   u={};
#   for k,v in pairs(t):
#     v,k=fun(k,v); u[k or (1+#u)]=v; end; return u end

# def sort(t, fun): # t; return `t`,  sorted by `fun` (default= `<`)
#   table.sort(t,fun)
#   return t

# def keys(t): # ss; return list of table keys, sorted
#   return sort(kap(t, function(k,_) return k end))