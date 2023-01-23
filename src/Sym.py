# -- ### SYM
# -- Summarize a stream of symbols.
# function SYM.new(i,at,txt) --> SYM; constructor
#   i.at, i.txt = at or 0, txt or "" -- col position and name
#   i.n   = 0
#   i.has = {}
#   i.most, i.mode = 0,nil end

# function SYM.add(i,x) --> nil;  update counts of things seen so far
#   if x ~= "?" then 
#    i.n = i.n + 1 
#    i.has[x] = 1 + (i.has[x] or 0)
#    if i.has[x] > i.most then
#      i.most,i.mode = i.has[x], x end end end 

# function SYM.mid(i,x) return i.mode end --> n; return the mode

# function SYM.div(i,x,    fun,e) --> n; return the entropy
#   function fun(p) return p*math.log(p,2) end
#   e=0; for _,n in pairs(i.has) do e = e + fun(n/i.n) end 
#   return -e end

# function SYM.rnd(i,x,n) return x end --> s; return `n` unchanged (SYMs do not get rounded)