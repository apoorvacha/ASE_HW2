# -- ## Misc support functions
# -- ### Numerics
# Seed=937162211
# function rint(lo,hi) return math.floor(0.5 + rand(lo,hi)) end --> n ; a integer lo..hi-1

# function rand(lo,hi) --> n; a float "x" lo<=x < x
#   lo, hi = lo or 0, hi or 1
#   Seed = (16807 * Seed) % 2147483647
#   return lo + (hi-lo) * Seed / 2147483647 end

# function rnd(n, nPlaces) --> num. return `n` rounded to `nPlaces`
#   local mult = 10^(nPlaces or 3)
#   return math.floor(n * mult + 0.5) / mult end 
import math

def rnd(n, nPlaces=3):
    mult = 10**(nPlaces or 3)
    return math.floor(n * mult + 0.5) / mult 

# -- ### Lists
# -- Note the following conventions for functions passed to  `map` or `kap`.
# -- - If a nil first argument is returned, that means :skip this result"
# -- - If a nil second argument is returned, that means place the result as position size+1 in output.
# -- - Else, the second argument is the key where we store function output.
# function map(t, fun,     u) --> t; map a function `fun`(v) over list (skip nil results) 
#   u={}; for k,v in pairs(t) do v,k=fun(v); u[k or (1+#u)]=v end;  return u end

def map(t,fun):
    u = {}
    for k,v in enumerate(t):
        v,k = fun(v)
        u[k or (1+len(u))] = v
    return u

# function kap(t, fun,     u) --> t; map function `fun`(k,v) over list (skip nil results) 
#   u={}; for k,v in pairs(t) do v,k=fun(k,v); u[k or (1+#u)]=v; end; return u end

def kap(t, fun):
    u = {}
    for k,v in enumerate(t):
        v,k = fun(k,v)
        u[k or (1+len(u))] = v
    
    return u

# function sort(t, fun) --> t; return `t`,  sorted by `fun` (default= `<`)
#   table.sort(t,fun); return t end

# function keys(t) --> ss; return list of table keys, sorted
#   return sort(kap(t, function(k,_) return k end)) end

# function push(t, x) --> any; push `x` to end of list; return `x` 
#   table.insert(t,x); return x end

# -- ### Strings
# function fmt(sControl,...) --> str; emulate printf
#   return string.format(sControl,...) end

# function oo(t) print(o(t)); return t end --> t; print `t` then return it
# function o(t,isKeys,     fun) --> s; convert `t` to a string. sort named keys. 
#   if type(t)~="table" then return tostring(t) end
#   fun= function(k,v) if not tostring(k):find"^_" then return fmt(":%s %s",o(k),o(v)) end end
#   return "{"..table.concat(#t>0 and not isKeys and map(t,o) or sort(kap(t,fun))," ").."}" end

# function coerce(s,    fun) --> any; return int or float or bool or string from `s`
#   function fun(s1)
#     if s1=="true" then return true elseif s1=="false" then return false end
#     return s1 end
#   return math.tointeger(s) or tonumber(s) or fun(s:match"^%s*(.-)%s*$") end

# function csv(sFilename,fun,    src,s,t) --> nil; call `fun` on rows (after coercing cell text)
#   src,s,t  = io.input(sFilename)
#   while true do
#     s = io.read()
#     if   s
#     then t={}; for s1 in s:gmatch("([^,]+)") do t[1+#t]=coerce(s1) end; fun(t)
#     else return io.close(src) end end end