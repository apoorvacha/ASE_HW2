import math

def rint(lo, hi):
    return math.floor(0.5 + rand(lo, hi))

def rand(lo, hi):
    lo, hi = lo or 0, hi or 1
    Seed = (16807 * Seed) % 2147483647
    return lo + (hi-lo) * Seed / 2147483647 end

def rnd(n, nPlaces=3):
    mult = 10**(nPlaces or 3)
    return math.floor(n * mult + 0.5) / mult

def cosine(a, b, c, x1, x2, y):
    x1 = (a**2 + c**2 - b**2) / (2*c)
    x2 = math.max(0, math.min(1, x1))
    y  = (a**2 - x2**2)**.5
    return x2, y

def map(t, fun, u):
    u = {}
    for k, v in enumerate(t):
        v, k = fun(v)
        u[k or (1+len(u))] = v
    return u

def kap(t, fun, u):
    u = {}
    for k, v in enumerate(t):
        v, k = fun(k, v)
        u[k or (1+len(u))] = v

def sort(t, fun):
    #Doubt

def lt(x):
    #Doubt

