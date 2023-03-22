# -- ### Lists
import math, random
# -- Push an item `x` onto  a list.    
# -- Return a list, sorted on `fun`.   
# -- Return a function sorting down on field `x`.    
# -- Return a function sorting up on field `x`.    
# -- Return one item at random.    
# -- Return many items, selected at random.   
# -- Map a function on  table (results in items 1,2,3...)    
# push = function(t,x) t[#t+1]=x; return x end
# sort = function(t,f) table.sort(t,f); return t end
# at   = function(x)   return function(t) return t[x] end end
# lt   = function(x)   return function(a,b) return a[x] < b[x] end end
# gt   = function(x)   return function(a,b) return a[x] > b[x] end end
# any  = function(t)   return t[rint(#t)] end
# # many = function(t,n,    u) u={}; for i=1,n do push(u, any(t)) end; return u end 
#  u = []
#     for i in range(1, n + 1):
#         u.append(any(t))
#     return u


def any(t):
    return random.choice(t)
    
def many(t,n):
    u = []
    for i in range(1, n + 1):
        u.append(any(t))
    return u


    
# map  = function(t, fun) return kap(t, function(_,v) return fun(v) end) end
# keys = function(t)      return sort(kap(t,function(k,_) return k end)) end

# -- Map a function on table (results in items key1,key2,...)
# function kap(t, fun,     u) 
#   u={}; for k,v in pairs(t) do v,k=fun(k,v); u[k or (1+#u)]=v; end; return u end

# -- Return the `p`-ratio item in `t`; e.g. `per(t,.5)` returns the medium.
# function per(t,p) 
#   p=math.floor(((p or .5)*#t)+.5); return t[m.max(1,m.min(#t,p))] end


def per(t, p):
    p = math.floor(((p or 0.5) * len(t)) + 0.5)
    return t[max(1, min(len(t), p))]

def kap(listOfCols, fun):
    u = {}
    for k, v in enumerate(listOfCols):
        v, k = fun(k, v)
        u[k or len(u)+1] = v
    return u

# -- Deep copy of a table `t`.
# function copy(t,    u) 
#   if  type(t)~="table" then return t end
#   u={}; for k,v in pairs(t) do u[k] = copy(v) end; return u end

# -- Return a portion of `t`; go,stop,inc defaults to 1,#t,1.
# -- Negative indexes are supported.
# function slice(t, go, stop, inc,    u) 
#   if go   and go   < 0 then go=#t+go     end
#   if stop and stop < 0 then stop=#t+stop end
#   u={}
#   for j=(go or 1)//1,(stop or #t)//1,(inc or 1)//1 do u[1+#u]=t[j] end
#   return u end
