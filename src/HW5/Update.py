# -- ## Update

# -- Update `data` with  row `t`. If `data.cols`
# -- does not exist, the use `t` to create `data.cols`.
# -- Otherwise, add `t` to `data.rows` and update the summaries in `data.cols`.
# -- To avoid updating skipped columns, we only iterate
# -- over `cols.x` and `cols.y`.
# function row(data,t)
#   if data.cols  then
#     push(data.rows,t)
#     for _,cols in pairs{data.cols.x, data.cols.y} do
#       for _,col in pairs(cols) do 
# 	     add(col, t[col.at]) end end 
#   else data.cols = COLS(t) end 
#   return data end

# -- Update one COL with `x` (values from one cells of one row).
# -- Used  by (e.g.) the `row` and `adds` function.
# -- `SYM`s just increment a symbol counts.
# -- `NUM`s store `x` in a finite sized cache. When it
# -- fills to more than `the.Max`, then at probability 
# -- `the.Max/col.n` replace any existing item
# -- (selected at random). If anything is added, the list
# -- may not longer be sorted so set `col.ok=false`.
# function add(col,x,  n)
#   if x ~= "?" then
#     n = n or 1
#     col.n = col.n + n
#     if   col.isSym
#     then col.has[x] = n + (col.has[x] or 0) 
#          if col.has[x] > col.most then
#            col.most, col.mode = col.has[x],x end 
#     else col.lo, col.hi = m.min(x,col.lo), m.max(x,col.hi) 
#       local all,pos
#       all = #col.has
#       pos = (all < the.Max and all+1) or (rand() < the.Max/col.n and rint(1,all))
#       if pos then
#         col.has[pos] = x
#         col.ok = false end end end end 

# -- Update a COL with multiple items from `t`. This is useful when `col` is being
# -- used outside of some DATA.
# function adds(col,t) 
#   for _,x in pairs(t or {}) do add(col,x) end; return col end

# -- Update a RANGE to cover `x` and `y`
# function extend(range,n,s)
#   range.lo = m.min(n, range.lo)
#   range.hi = m.max(n, range.hi)
#   add(range.y, s) end
