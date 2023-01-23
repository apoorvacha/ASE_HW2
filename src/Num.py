# -- ### NUM
# -- Summarizes a stream of numbers.
# function NUM.new(i,at,txt) --> NUM;  constructor; 
#   i.at, i.txt = at or 0, txt or "" -- column position and name
#   i.n, i.mu, i.m2 = 0, 0, 0
#   i.lo, i.hi = math.huge, -math.huge 
#   i.w = i.txt:find"-$" and -1 or 1 end

# function NUM.add(i,n,    d) --> NUM; add `n`, update lo,hi and stuff needed for standard deviation
#   if n ~= "?" then
#     i.n  = i.n + 1
#     d = n - i.mu
#     i.mu = i.mu + d/i.n
#     i.m2 = i.m2 + d*(n - i.mu)
#     i.lo = math.min(n, i.lo)
#     i.hi = math.max(n, i.hi) end end

# function NUM.mid(i,x) return i.mu end --> n; return mean

# function NUM.div(i,x)  --> n; return standard deviation using Welford's algorithm http://.ly/nn_W
#     return (i.m2 <0 or i.n < 2) and 0 or (i.m2/(i.n-1))^0.5  end

# function NUM.rnd(i,x,n) return x=="?" and x or rnd(x,n) end --> n; return number, rounded