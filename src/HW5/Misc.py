import math, json
import re, copy
from Start import the
# from Data import *

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

def any(t):
    return t[rint(len(t))]

def many(t,n):
    u = {}
    for i in range(1,n):
        u[1+len(u)] = any(t)
    return u
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
    return t[rint(0, len(t) - 1)]

def many(t, n):
    u = []
    for i in range(n):
        u.append(any(t))
    return u

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
# Main

def settings(s, t):
    return dict(re.findall(r"\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)", s))

def transpose(t):
    u = []
    for i in range(len(t[0])):
        row = []
        for j in range(len(t)):
            row.append(t[j][i])
        u.append(row)
    return u

def repCols(cols):
    cols1 = copy.deepcopy(cols)
    for col in cols1:
        col[-1] = str(col[0]) + ":" + str(col[-1])
        for j in range(1, len(col)):
            col[j-1] = col[j]
        col.pop()
    cols1.insert(0, ["Num" + str(i) for i in range(1, len(cols1[0]) + 1)])
    cols1[0][-1] = "thingX"
    return Data(cols1)

def repRows(t, rows):
    rows = copy.deepcopy(rows)
    for j, s in enumerate(rows[-1]):
        rows[0][j] = str(rows[0][j]) + ":" + str(s)
    rows.pop()

    for n, row in enumerate(rows):
        if n == 0:
            row.append("thingX")
        else:

            u = t["rows"][len(t["rows"]) - n]
            row.append(u[len(u)-1])
        print(rows)
    return Data(rows)

def dofile(sFile):
    file = open(sFile, "r", encoding="utf-8")
    text = (
        re.findall(r"(?<=return )[^.]*", file.read())[0]
        .replace("{", "[")
        .replace("}", "]")
        .replace("=", ":")
        .replace("[\n", "{\n")
        .replace(" ]", " }")
        .replace("'", '"')
        .replace("_", '"_"')
    )
    file.close()
    file_json = json.loads(re.sub(r"(\w+):", r'"\1":', text)[:-2] + "}")
    return file_json

def repgrid(sFile):

    t = dofile(sFile)
    rows = repRows(t, transpose(t["cols"]))
    cols = repCols(t["cols"])
    show(rows.cluster())
    show(cols.cluster())


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
