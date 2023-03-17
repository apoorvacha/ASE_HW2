# -- ## Query
import math
from List import *

# -- A query that returns contents of a column. If `col` is a `NUM` with
# -- unsorted contents, then sort before return the contents.
# -- Called by (e.g.) the `mid` and `div` functions.
# function has(col)
#   if not col.isSym and not col.ok then sort(col.has) end 
#   col.ok = true -- the invariant here is that "has" is ready to be shared.
#   return col.has end

def has(col):
    if not hasattr(col, "isSym") and not col.ok:
        if isinstance(col.has, dict):
            col.has = dict(sorted(col.has.items(), key = lambda item: item[1]))
        else:
            col.has.sort()
    col.ok = True
    return col.has
    
# -- A query that  returns a `cols`'s central tendency  
# -- (mode for `SYM`s and median for `NUM`s). Called by (e.g.) the `stats` function.
# function mid(col,    mode,most)
#   return col.isSym and col.mode or per(has(col), .5) end 


def mid(col):
    return col.mode if hasattr(col, "isSym") else per(has(col), 0.5)

# -- A query that returns a `col`'s deviation from central tendency    
# -- (entropy for `SYM`s and standard deviation for `NUM`s)..
# function div(col,    e)
#   if   col.isSym 
#   then e=0
#        for _,n in pairs(col.has) do e= e-n/col.n*m.log(n/col.n,2) end
#        return e
#   else return (per(has(col),.9) - per(has(col), .1))/2.58 end end

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
        
# -- A query that returns `mid` or `div` of `cols` (defaults to `data.cols.y`).
# function stats(data,  fun,cols,nPlaces,     tmp)
#   cols= cols or data.cols.y
#   tmp = kap(cols,
#             function(k,col) return rnd((fun or mid)(col),nPlaces), col.txt end)
#   tmp["N"] = #data.rows
#   return tmp,map(cols,mid)  end

def stats(data, fun = None, cols = None, nPlaces = 2):
    cols = cols or data.cols.y
    def callBack(k, col):
        col = col.col
        return round((fun or mid)(col), nPlaces), col.txt
    tmp = kap(cols, callBack)
    tmp["N"] = len(data.rows)
    return tmp, map(mid, cols)

# -- A query that normalizes `n` 0..1. Called by (e.g.) the `dist` function.
# function norm(num,n)
#   return x=="?" and x or (n - num.lo)/(num.hi - num.lo + 1/m.huge) end

# -- A query that returns the score a distribution of symbols inside a SYM.
# function value(has,  nB,nR,sGoal,    b,r)
#   sGoal,nB,nR = sGoal or true, nB or 1, nR or 1
#   b,r = 0,0
#   for x,n in pairs(has) do
#     if x==sGoal then b = b + n else r = r + n end end
#   b,r = b/(nB+1/m.huge), r/(nR+1/m.huge)
#   return b^2/(b+r) end

# -- A query that returns the distances 0..1 between rows `t1` and `t2`.   
# -- If any values are unknown, assume max distances.
# function dist(data,t1,t2,  cols,    d,n,dist1)
#   function dist1(col,x,y)
#     if x=="?" and y=="?" then return 1 end
#     if   col.isSym
#     then return x==y and 0 or 1 
#     else x,y = norm(col,x), norm(col,y)
#          if x=="?" then x= y<.5 and 1 or 1 end	
#          if y=="?" then y= x<.5 and 1 or 1 end	
#          return m.abs(x-y) end 
#   end --------------
#   d, n = 0, 1/m.huge	
#   for _,col in pairs(cols or data.cols.x) do
#     n = n + 1
#     d = d + dist1(col, t1[col.at], t2[col.at])^the.p end 
#   return (d/n)^(1/the.p) end

# -- A query that returns true if `row1` is better than another.
# -- This is Zitzler's indicator predicate that
# -- judges the domination status 
# -- of pair of individuals by running a “what-if” query. 
# -- It checks what we lose if we (a) jump from one 
# -- individual to another (see `s1`), or if we (b) jump the other way (see `s2`).
# -- The jump that losses least indicates which is the best row.
# function better(data,row1,row2,    s1,s2,ys,x,y) 
#   s1,s2,ys,x,y = 0,0,data.cols.y
#   for _,col in pairs(ys) do
#     x  = norm(col, row1[col.at] )
#     y  = norm(col, row2[col.at] )
#     s1 = s1 - m.exp(col.w * (x-y)/#ys)
#     s2 = s2 - m.exp(col.w * (y-x)/#ys) end
#   return s1/#ys < s2/#ys end

def better(data,row1,row2):
    s1,s2,ys,x,y = 0,0,data.cols.y
    for _,col in enumerate(ys) :
        x = math.norm(col, row1[col.at])
        y = math.norm(col, row2[col.at])

        s1 = s1 - math.exp(col.w * (x - y) / len(ys))
        s2 = s2 - math.exp(col.w * (y - x) / len(ys))
    return s1/len(ys) < s2/len(ys) 