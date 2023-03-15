# -- ## Clustering

# -- Cluster `rows` into two sets by
# -- dividing the data via their distance to two remote points.
# -- To speed up finding those remote points, only look at
# -- `some` of the data. Also, to avoid outliers, only look
# -- `the.Far=.95` (say) of the way across the space. 
# function half(data,  rows,cols,above)
#   local left,right,far,gap,some,proj,cos,tmp,A,B,c = {},{}
#   function gap(r1,r2) return dist(data, r1, r2, cols) end
#   function cos(a,b,c) return (a^2 + c^2 - b^2)/(2*c) end
#   function proj(r)    return {row=r, x=cos(gap(r,A), gap(r,B),c)} end
#   rows = rows or data.rows
#   some = many(rows,the.Halves)
#   A    = (the.Reuse and above) or any(some)
#   tmp  = sort(map(some,function(r) return {row=r, d=gap(r,A)} end ),lt"d")
#   far  = tmp[(#tmp*the.Far)//1]
#   B,c  = far.row, far.d
#   for n,two in pairs(sort(map(rows,proj),lt"x")) do
#     push(n <= #rows/2 and left or right, two.row) end
#   return left,right,A,B,c end

# -- Cluster, recursively, some `rows` by  dividing them in two, many times
# function tree(data,  rows,cols,above,     here)
#   rows = rows or data.rows
#   here = {data=DATA.clone(data,rows)}
#   if #rows >= 2*(#data.rows)^the.min then
#     local left,right,A,B = half(data, rows, cols, above)
#     here.left  = tree(data, left,  cols, A)
#     here.right = tree(data, right, cols, B) end
#   return here end 

# -- Cluster can be displayed by this function.
# function showTree(tree,  lvl,post)
#   if tree then 
#     lvl  = lvl or 0
#     io.write(fmt("%s[%s] ",("|.. "):rep(lvl), #(tree.data.rows)))
#     print((lvl==0 or not tree.left) and o(stats(tree.data)) or "")
#     showTree(tree.left, lvl+1)
#     showTree(tree.right,lvl+1) end end