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

# function sort(t, fun) --> t; return `t`,  sorted by `fun` (default= `<`)
#   table.sort(t,fun); return t end

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

# for n,row in pairs(rows) do
#     if n==1 then push(row,"thingX") else
#       u=t.rows[#t.rows - n + 2]
#       push(row, u[#u]) end end
#   return  DATA(rows) end
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

# -- ## Miscellaneous Support Code
# -- ### Meta

# -- Return self
# function itself(x) return x end

# -- ### Maths

# -- Round numbers
# function rnd(n, nPlaces) 
#   local mult = 10^(nPlaces or 2)
#   return math.floor(n * mult + 0.5) / mult end

# -- Random number generation.
# Seed=937162211 -- seed
# function rint(nlo,nhi)  -- random ints  
#   return m.floor(0.5 + rand(nlo,nhi)) end

# function rand(nlo,nhi) -- random floats
#   nlo, nhi = nlo or 0, nhi or 1
#   Seed = (16807 * Seed) % 2147483647
#   return nlo + (nhi-nlo) * Seed / 2147483647 end

# -- Non-parametric effect-size test
# --  M.Hess, J.Kromrey. 
# --  Robust Confidence Intervals for Effect Sizes: 
# --  A Comparative Study of Cohen's d and Cliff's Delta Under Non-normality and Heterogeneous Variances
# --  American Educational Research Association, San Diego, April 12 - 16, 2004    
# --  0.147=  small, 0.33 =  medium, 0.474 = large; med --> small at .2385
# function cliffsDelta(ns1,ns2) 
#   if #ns1 > 256     then ns1 = many(ns1,256) end
#   if #ns2 > 256     then ns2 = many(ns2,256) end
#   if #ns1 > 10*#ns2 then ns1 = many(ns1,10*#ns2) end
#   if #ns2 > 10*#ns1 then ns2 = many(ns2,10*#ns1) end
#   local n,gt,lt = 0,0,0
#   for _,x in pairs(ns1) do
#     for _,y in pairs(ns2) do
#       n = n + 1
#       if x > y then gt = gt + 1 end
#       if x < y then lt = lt + 1 end end end
#   return m.abs(lt - gt)/n > the.cliffs end

# -- Given two tables with the same keys, report if their
# -- values are different.
# function diffs(nums1,nums2)
#   return kap(nums1, function(k,nums) 
#               return cliffsDelta(nums.has,nums2[k].has),nums.txt end) end

# -- ### String to thing

# -- Coerce string to boolean, int,float or (failing all else) strings.
# function coerce(s,    fun) 
#   function fun(s1)
#     if s1=="true" then return true elseif s1=="false" then return false end
#     return s1 end
#   return math.tointeger(s) or tonumber(s) or fun(s:match"^%s*(.-)%s*$") end

# -- Split a string `s`  on commas.
# function cells(s,    t)
#   t={}; for s1 in s:gmatch("([^,]+)") do t[1+#t] = coerce(s1) end; return t end

# -- Run `fun` for all lines in a file.
# function lines(sFilename,fun,    src,s) 
#   src = io.input(sFilename)
#   while true do
#     s = io.read(); if s then fun(s) else return io.close(src) end end end

# -- Run `fun` on the cells  in each row of a csv file.
# function csv(sFilename,fun)
#   lines(sFilename, function(line) fun(cells(line)) end) end