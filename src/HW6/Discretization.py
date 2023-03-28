from Col import COL
from Query import *

from Data import *
import Update as upd

import math
from copy import deepcopy
from Range import *
import Misc, Rule
  
def bins(cols, rowss):
    for _, col in enumerate(cols):
        ranges = {}
        index = 0 
        n_ranges = {}
        n_ranges_list = []
        for y, rows in rowss.items():
            for _, row in enumerate(rows):

                if (isinstance(col, COL)):
                   col = col.col
                   
                x = row[col.at]

                if x != '?':
                    k = int(bin(col, float(x) ))
                    if k in ranges:
                        ranges[k] = ranges[k] 
                    else:
                        ranges[k] = RANGE(col.at, col.txt, float(x))
                    upd.extend(ranges[k], float(x), y)

        ranges = {key: value for key, value in sorted(ranges.items(), key=lambda x: x[1].lo)}

        out = []

        for r in ranges:
            n_ranges[index] = ranges[r]
            index = index+1

        if(hasattr(col, "isSym") and col.isSym):
            out.append(n_ranges_list )
        
    return out

def bin(col, x):

    if x=="?" or hasattr(col, "isSym"):
        return x
    tmp = (col.hi - col.lo)/(16 - 1)
    
    if col.hi == col.lo:
        return 1 
    else:
        return  math.floor(x/tmp+0.5)*tmp

min = -float("inf")
max = float("inf")

def mergeAny(ranges0):

    def noGaps(t):
        for j in range(1, len(t)):
            t[j].lo = t[j-1].hi
        t[0].lo = min
        t[-1].hi = max
        return t

    ranges1, j , left, right , y= [], 0

    while j < len(ranges0):
        left, right = ranges0[j], ranges0[j+1]
        if right:
            y = merge2(left.y, right.y)
            if y:
               j = j+1
               left.hi, left.y = right.hi, y
        ranges1.append(left)
        j = j+1
    
    if len(ranges1) == len(ranges0):
        return noGaps(ranges0)
    else : 
       mergeAny(ranges1)

def merge2(col1, col2):

    new = merge(col1, col2)

    if div(new) <= (div(col1)*col1.n + div(col2)*col2.n)/new.n:
        return new

def merge(col1, col2):

    new = deepcopy(col1)
    if hasattr(col1, "isSym") and col1.isSym:
        for x, n in col2.has.items():
            upd.add(new, x, n)
    else:
        for n in col2.has:
            upd.add(new, n)

        new.lo = min(col1.lo, col2.lo)
        new.hi = max(col1.hi, col2.hi)

    return new

def xpln(data,best,rest):
    
    def v(has):
        return value(has, len(best.rows) , len(rest.rows), "best")
    def score(ranges):
        rule = Rule.Rule(ranges, maxSizes)
        if rule:
            Misc.oo(showRule(rule))
            bestr= selects(rule, best.rows)
            restr= selects(rule, rest.rows)
            if len(bestr)+ len(restr) >0 :
                return v({"best" : len(bestr), "rest" : len(restr)}),rule
    tmp,maxSizes = [], []
    for _, ranges in enumerate(bins(data.cols.x,{"best":best.rows, "rest":rest.rows})):
        maxSizes[ranges[0].txt] = len(ranges)
        print("")
        for _,range in enumerate(ranges):
            print(range.txt, range.lo, range.hi)
            val= v(range.y.has)
            tmp.append({"range" : range, "max" : len(ranges), "val": val})
            
    rule,most=firstN(sorted(tmp,key=lambda x: x["val"], reverse=True), score)
    return rule, most


def firstN(sortedRanges,scoreFun):
    print("")
    def callback():
        for r in sortedRanges:
            print(r["range"].txt, r["range"].lo, r["range"].hi, round(r["val"], 2), r["range"].y.has)
        return sortedRanges[0]["val"] 
    first = callback()
    def useful(range):
        if range.val >0.5 and range.val> first/10:
            return range
    sortedRanges = list(filter(useful, sortedRanges))
    most = -1
    out = None
    for n in (1, len(sortedRanges)):
       
        for r in sortedRanges[:n + 1]:
            tmp, rule = scoreFun(r["range"])
        # tmp,rule = scoreFun(map(slice(sortedRanges,1,n),on"range"))
        if tmp> most:
            tmp= out
        else :
            out = rule
            most = tmp
    return out, most

def showRule(rule):

    def pretty(range):
        return range["lo"] if range["lo"] == range["hi"] else [range["lo"], range["hi"]]

    def merges(attr, ranges):
        return list(map(merge(sorted(ranges, key=lambda r: r['lo'])),pretty)), attr

    def merge(t0):
        t, j = [], 0
        while j < len(t0):
            left, right = t0[j], t0[j+1] if j+1 < len(t0) else t0[j], None
            if right and left['hi'] == right['lo']:
                left['hi'] = right['hi']
                j += 1
            t.append({'lo': left['lo'], 'hi': left['hi']})
            j += 1
        return t if len(t0) == len(t) else merge(t)

    return Misc.kap(rule, merges)

def selects(rule, rows):
    def disjunction(ranges, row):
        for range in ranges:
            lo = int(range['lo'])
            hi = int(range['hi'])
            at = int(range['at'])
            x = row[at]
            if x == "?":
                return True
            x = float(x)
            if lo == hi and lo == x:
                return True
            if lo <= x and x < hi:
                return True
        return False

    def conjunction(row):
        for ranges in rule.values():
            if not disjunction(ranges, row):
                return False
        return True

    return [r for r in rows if conjunction(r)]

# function  showRule(rule,    merges,merge,pretty)
#   function pretty(range)
#     return range.lo==range.hi and range.lo or {range.lo, range.hi} end
#   function merges(attr,ranges) 
#    return map(merge(sort(ranges,lt"lo")),pretty),attr end
#   function merge(t0)
#     local t,j, left,right={},1
#     while j<=#t0 do
#       left,right = t0[j],t0[j+1]
#       if right and left.hi == right.lo then left.hi = right.hi; j=j+1 end
#       push(t, {lo=left.lo, hi=left.hi})
#       j=j+1 end
#     return #t0==#t and t or merge(t) end 
#   return kap(rule,merges) end

# function selects(rule,rows,    disjunction,conjunction)
#   function disjunction(ranges,row,    x) 
#     for _,range in pairs(ranges) do
#       local lo, hi, at = range.lo, range.hi, range.at
#       x = row[at]
#       if x == "?"         then return true end
#       if lo==hi and lo==x then return true end
#       if lo<=x  and x< hi then return true end end 
#     return false end 
#   function conjunction(row)
#     for _,ranges in pairs(rule) do 
#       if not disjunction(ranges,row) then return false end end
#     return true end 
#   return map(rows, function(r) if conjunction(r) then return r end end) end




