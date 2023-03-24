import math, json
import re, copy
from Start import the
import math, random

def show(node, what, cols, nPlaces, lvl=None):
    if node:
        lvl = lvl or 0
        print("| " * lvl, str(len(node["data"].rows)), " ")
        if not node.get("left", None) or lvl == 0:
            print(o(node["data"].stats("mid", node["data"].cols.y, nPlaces)))
        else:
            print("")
        show(node.get("left", None), what, cols, nPlaces, lvl+1)
        show(node.get("right", None), what, cols, nPlaces, lvl+1)

# Numeric Functions

def rint(lo, hi):
    return math.floor(0.5 + rand(lo, hi))

# many = function(t,n,    u) u={}; for i=1,n do push(u, any(t)) end; return u end 
def rand(lo=0, hi=1):
    lo, hi = lo or 0, hi or 1
    Seed = (16807 * the["seed"]) % 2147483647
    return lo + (hi-lo) * Seed / 2147483647

def cosine(a, b, c):
    x1 = (a**2 + c**2 - b**2) / (2*c)
    x2 = max(0, min(1, x1))
    y  = (a**2 - x2**2)**.5
    return x2, y


def sort(t):
    #Doubt
    return t

def lt(x):
    def fun(a, b):
        return a[x] < b[x]

def keys(t):
    #Doubt
    pass

def push(t, x):
    t.append(x)

def any(t):
    return random.choice(t)
    
def many(t,n):
    u = []
    for i in range(1, n + 1):
        u.append(any(t))
    return u

def per(t, p):
    p = math.floor(((p or 0.5) * len(t)) + 0.5)
    return t[max(1, min(len(t), p))]

# String Functions

def coerce(s): #Doubt
    if s == "true":
        return True
    elif s == "false":
        return False
    elif re.search(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?$", s) is not None:
        return float(s)
    else:
        return s

def rnd(n, nPlaces=3):
    mult = 10**(nPlaces or 3)
    return math.floor(n * mult + 0.5) / mult 


def map(t,fun):
    u = {}
    for k,v in enumerate(t):
        v,k = fun(v)
        print(v,k)
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


def cliffs_delta(ns1, ns2):

    if len(ns1) > 256:
        ns1 = many(ns1, 256)
    if len(ns2) > 256:
        ns2 = many(ns2, 256)
    if len(ns1) > 10 * len(ns2):
        ns1 = many(ns1, 10 * len(ns2))
    if len(ns2) > 10 * len(ns1):
        ns2 = many(ns2, 10 * len(ns1))

    n, gt, lt = 0, 0, 0
    for x in ns1:
        for y in ns2:
            n += 1
            if x > y:
                gt += 1
            if x < y:
                lt += 1

    return abs(lt - gt) / n > 0.147

def diffs(nums1, nums2):
    def kap(nums, fn):
        return [fn(k, v) for k, v in enumerate(nums)]
    return kap(nums1, lambda k, nums: (cliffs_delta(nums.col.has, nums2[k].col.has), nums.col.txt))
