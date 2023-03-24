# -- ## Query
import math
from List import *

def has(col):
    if not hasattr(col, "isSym") and not col.ok:
        if isinstance(col.has, dict):
            col.has = dict(sorted(col.has.items(), key = lambda item: item[1]))
        else:
            col.has.sort()
    col.ok = True
    return col.has



def mid(col):
    return col.mode if hasattr(col, "isSym") else per(has(col), 0.5)


def div(col):
    if hasattr(col, "isSym"):
        e = 0
        if isinstance(col.has, dict):
            for n in col.has.values():
                e = e - n/col.n * math.log(n/col.n, 2)
        else:
            for n in col.has:
                e = e - n/col.n * math.log(n/col.n, 2)
        return e
    else:
        return (per(has(col),.9) - per(has(col), .1)) / 2.58


def stats(data, fun = None, cols = None, nPlaces = 2):
    cols = cols or data.cols.y
    def callBack(k, col):
        col = col.col
        return round((fun or mid)(col), nPlaces), col.txt
    tmp = kap(cols, callBack)
    tmp["N"] = len(data.rows)
    return tmp, map(mid, cols)

def norm(num, n):
    if(n == '?'):
        return n 
    else :
        return (float(n)-num.lo) / (num.hi - num.lo + 1 / float('inf'))

def better(data,row1,row2):
    s1,s2,ys,x,y = 0,0,data.cols.y, None, None
    for _,col in enumerate(ys) :
        x = norm(col.col, row1[col.col.at])
        y = norm(col.col, row2[col.col.at])

        s1 = s1 - math.exp(col.col.w * (x - y) / len(ys))
        s2 = s2 - math.exp(col.col.w * (y - x) / len(ys))
    return s1/len(ys) < s2/len(ys) 

def dist1(col, x, y):
        if x == "?" and y == "?":
            return 1
        if hasattr(col, "isSym"):
            return 0 if x==y else 1
        else:
            x, y = norm(col, x), norm(col, y)
            if x == "?":
                x = 1 if y<0.5 else 0
            if y == "?":
                y = 1 if x<0.5 else 0
        
        return abs(x - y)

def dist(data, row1, row2, cols=None):
    n, d = 0, 0
    for _, col in enumerate(cols or data.cols.x):
        n = n + 1
        val = dist1(col.col,row1[col.col.at], row2[col.col.at])
        d = d + val ** 2
    return (d / n) ** (1 / 2)

def value(has, nB = 1, nR = 1, sGoal = True):
    b, r = 0, 0
    for x, n in has.items():
        if x == sGoal:
            b = b + n
        else:
            r = r + n
    b,r = b/(nB+1/float("inf")), r/(nR+1/float("inf"))
    return (b ** 2) / (b + r)