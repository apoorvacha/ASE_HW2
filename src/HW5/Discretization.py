# -- ## Discretization

# -- Return RANGEs that distinguish sets of rows (stored in `rowss`).
# -- To reduce the search space,
# -- values in `col` are mapped to small number of `bin`s.
# -- For NUMs, that number is `the.bins=16` (say) (and after dividing
# -- the column into, say, 16 bins, then we call `mergeAny` to see
# -- how many of them can be combined with their neighboring bin).
# function bins(cols,rowss)
#   local out = {}
#   for _,col in pairs(cols) do
#     local ranges = {}
#     for y,rows in pairs(rowss) do
#       for _,row in pairs(rows) do
#         local x,k = row[col.at]
#         if x ~= "?" then
#           k = bin(col,x)
#           ranges[k] = ranges[k] or RANGE(col.at,col.txt,x)
#           extend(ranges[k], x, y) end end end
#     ranges = sort(map(ranges,itself),lt"lo")
#     out[1+#out] = col.isSym and ranges or mergeAny(ranges) end
#   return out end

# -- Map `x` into a small number of bins. `SYM`s just get mapped
# -- to themselves but `NUM`s get mapped to one of `the.bins` values.
# -- Called by function `bins`.
# function bin(col,x,      tmp)
#   if x=="?" or col.isSym then return x end
#   tmp = (col.hi - col.lo)/(the.bins - 1)
#   return col.hi == col.lo and 1 or m.floor(x/tmp + .5)*tmp end

# -- Given a sorted list of ranges, try fusing adjacent items
# -- (stopping when no more fuse-ings can be found). When done,
# -- make the ranges run from minus to plus infinity
# -- (with no gaps in between).
# -- Called by function `bins`.
# function mergeAny(ranges0,     noGaps)
#   function noGaps(t)
#     for j = 2,#t do t[j].lo = t[j-1].hi end
#     t[1].lo  = -m.huge
#     t[#t].hi =  m.huge
#     return t 
#   end ------
#   local ranges1,j,left,right,y = {},1
#   while j <= #ranges0 do
#     left, right = ranges0[j], ranges0[j+1]
#     if right then
#       y = merge2(left.y, right.y)
#       if y then
#         j = j+1 -- next round, skip over right.
#         left.hi, left.y = right.hi, y end end
#     push(ranges1,left)
#     j = j+1 
#   end
#   return #ranges0==#ranges1 and noGaps(ranges0) or mergeAny(ranges1) end

# -- If the whole is as good (or simpler) than the parts,
# -- then return the 
# -- combination of 2 `col`s.
# -- Called by function `mergeMany`.
# function merge2(col1,col2,   new)
#   new = merge(col1,col2)
#   if div(new) <= (div(col1)*col1.n + div(col2)*col2.n)/new.n then
#     return new end end

# -- Merge two `cols`. Called by function `merge2`.
# function merge(col1,col2,    new)
#   new = copy(col1)
#   if   col1.isSym 
#   then for x,n in pairs(col2.has) do add(new,x,n) end
#   else for _,n in pairs(col2.has) do add(new,n)   end
#        new.lo = m.min(col1.lo, col2.lo)
#        new.hi = m.max(col1.hi, col2.hi) end 
#   return new end

   