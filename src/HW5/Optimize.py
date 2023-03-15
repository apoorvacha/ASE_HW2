# -- ## Optimization

# -- Recursively prune the worst half the data. Return
# -- the survivors and some sample of the rest.
# function sway(data,     worker,best,rest)
#   function worker(rows,worse,  above)
#     if   #rows <= (#data.rows)^the.min 
#     then return rows, many(worse, the.rest*#rows) 
#     else local l,r,A,B = half(data, rows, cols, above)
#          if better(data,B,A) then l,r,A,B = r,l,B,A end
#          map(r, function(row) push(worse,row) end) 
#          return worker(l,worse,A) end 
#   end ----------------------------------
#   best,rest = worker(data.rows,{})
#   return DATA.clone(data,best), DATA.clone(data,rest) end 