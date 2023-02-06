import math

def rnd(n, nPlaces=3):
    mult = 10**(nPlaces or 3)
    return math.floor(n * mult + 0.5) / mult 


def map(t,fun):
    u = {}
    for k,v in enumerate(t):
        v,k = fun(v)
        u[k or (1+len(u))] = v
    return u

def kap(t, fun):
    u = {}
    for k,v in enumerate(t):
        v,k = fun(k,v)
        u[k or (1+len(u))] = v
    
    return u

def oo(t):
    print(o(t))
    return t

def o(t, isKeys=None):
    return str(t)
