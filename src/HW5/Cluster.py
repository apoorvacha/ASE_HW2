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

import Query , List
from Start import the
def half(self, data):
    left =[]
    right =[]
    # far,gap,some,proj,cos,tmp,A,B,c = {},{}
    def gap(r1,r2):
         return Query.dist(data, r1, r2, cols) 
    def cos(a,b,c):
         return (a**2 + c**2 - b**2)/(2*c) 
    def proj(r) :
         return {"row":r, "x":cos(gap(r,A), gap(r,B),c)}
    rows = rows or data.rows
    some = List.many(rows,the["Halves"])
    A    = (the["Reuse"] and above) or any(some)
    tmp = sorted([{"row": r, "d": gap(r, A)} for r in some], key=lambda x: x["d"])
    far = tmp[int(len(tmp)*the["Far"])//1 ]
    B,c  = far.row, far.d
    for n, two in enumerate(sorted(map(proj, rows), key=lambda x: x["x"])):
            if n <= (len(rows)) / 2:
                left.append(two["row"])
            else:
                right.append(two["row"])
    return left, right, A, B, c

# -- Cluster, recursively, some `rows` by  dividing them in two, many times
# function tree(data,  rows,cols,above,     here)
#   rows = rows or data.rows
#   here = {data=DATA.clone(data,rows)}
#   if #rows >= 2*(#data.rows)^the.min then
#     local left,right,A,B = half(data, rows, cols, above)
#     here.left  = tree(data, left,  cols, A)
#     here.right = tree(data, right, cols, B) end
#   return here end 

def tree(data, rows=None, cols=None, above=None):
    rows = rows or data.rows
    here = {"data": data.clone(data, rows)}
    if len(rows) >= 2 * (len(data.rows) ** 0.5):
        left, right, A, B, _ = half(data, rows, cols, above)
        here["left"] = tree(data, left, cols, A)
        here["right"] = tree(data, right, cols, B)
    return here

# -- Cluster can be displayed by this function.
# function showTree(tree,  lvl,post)
#   if tree then 
#     lvl  = lvl or 0
#     io.write(fmt("%s[%s] ",("|.. "):rep(lvl), #(tree.data.rows)))
#     print((lvl==0 or not tree.left) and o(stats(tree.data)) or "")
#     showTree(tree.left, lvl+1)
#     showTree(tree.right,lvl+1) end end

def show_tree(tree, lvl=0, post=None):
    if tree:
        print("{}[{}]".format("|.. " * lvl, len(tree["data"].rows)), end="")
        if lvl == 0 or ("left" not in tree):
            print(Query.stats(tree["data"]))
        else:
            print("")
        show_tree(tree["left"] if "left" in tree else None, lvl + 1)
        show_tree(tree["right"] if "right" in tree else None, lvl + 1)