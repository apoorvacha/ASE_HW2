from HW3 import Misc
from HW3 import Cols
from HW3 import Rows
import math, csv
from typing import List, Union

def csv_content(src):
    res = []
    with open(src, mode='r') as file:
        csvFile = csv.reader(file)
        res.append(csvFile)

    return res

class Data:

# -- ### DATA
# -- Store many rows, summarized into columns
# function DATA.new(i,src,     fun) --> DATA; A container of `i.rows`, to be summarized in `i.cols`
#   i.rows, i.cols = {}, nil
#   fun = function(x) i:add(x) end
#   if type(src) == "string" then csv(src,fun)  -- load from a csv file on disk
#                            else map(src or {}, fun)  --  load from a list
#                            end end
    def __init__(self,src):
        self.rows = []
        self.cols = None

        if type(src) == str:
            csv_list = csv_content(src)
            for row in csv_list:
                row_cont = []
                for val in row:
                    row_cont.append(val.strip())
                self.add(row_cont)

        elif type(src) == List[str]:  # else we were passed the columns as a string
            self.add(src)

# function DATA.add(i,t) --> nil; add a new row, update column headers
#   if   i.cols          --] true if we have already seen the column names
#   then t = t.cells and t or ROW(t) -- ensure is a ROW, reusing old rows in the are passed in
#        -- t =ROW(t.cells and t.cells or t) -- make a new ROW
#        push(i.rows, t) -- add new data to "i.rows"
#        i.cols:add(t)  -- update the summary information in "ic.ols"
#   else i.cols=COLS(t)  end end --  here, we create "i.cols" from the first row
    def add(self,t:list[str]):

        if (self.cols):
            row = Rows.Rows(t)
            self.rows.append(row)
            self.cols.add(row)
        else:
            self.cols = Cols.Cols(t)

# function DATA.clone(i,  init,     data) --> DATA; return a DATA with same structure as `ii. 
#   data=DATA({i.cols.names})
#   map(init or {}, function(x) data:add(x) end)
#   return data end
    def clone(self,init= None):
        if not init:
            init = []
        data = Data({self.cols.names})
        return data

# function DATA.stats(i,  what,cols,nPlaces,fun) --> t; reports mid or div of cols (defaults to i.cols.y)
#   function fun(k,col) return col:rnd(getmetatable(col)[what or "mid"](col),nPlaces),col.txt end
#   return kap(cols or i.cols.y, fun) end
    def stats(self, what, cols: Cols, n_places):
        def fun(k, col):
            return col.rnd(getattr(col, what), n_places), col.txt
        return Misc.kap(cols, fun)

# function DATA.better(i,row1,row2,    s1,s2,ys,x,y) --> bool; true if `row1` dominates (via Zitzler04).
#   s1,s2,ys,x,y = 0,0,i.cols.y
#   for _,col in pairs(ys) do
#     x  = col:norm( row1.cells[col.at] )
#     y  = col:norm( row2.cells[col.at] )
#     s1 = s1 - math.exp(col.w * (x-y)/#ys)
#     s2 = s2 - math.exp(col.w * (y-x)/#ys) end
#   return s1/#ys < s2/#ys end
    def better(self, row1, row2,s1,s2,ys,x,y):
        s1, s2, ys = 0, 0, self.cols.y
        for _,col in enumerate(ys):
            x = col.norm(row1[col.at])
            y = col.norm(row2[col.at])
            s1 = s1 - math.exp(col.w * (x - y) / len(ys))
            s2 = s2 - math.exp(col.w * (y - x) / len(ys))
        
        return s1/len(ys) < s2/len(ys)

# function DATA.dist(i,row1,row2,  cols,      n,d) --> n; returns 0..1 distance `row1` to `row2`
#   n,d = 0,0
#   for _,col in pairs(cols or i.cols.x) do
#     n = n + 1
#     d = d + col:dist(row1.cells[col.at], row2.cells[col.at])^the.p end
#   return (d/n)^(1/the.p) end
    def dist(self, row1, row2, cols, n, d):
        n, d = 0, 0
        for _, col in enumerate(cols or self.cols.x):
            n = n + 1
            d = d + col.dist(row1[col.at], row2[col.at]) ** 2
        return (d / n) ** (1 / 2)

# function DATA.around(i,row1,  rows,cols) --> t; sort other `rows` by distance to `row`
#   return sort(map(rows or i.rows, 
#                   function(row2)  return {row=row2, dist=i:dist(row1,row2,cols)} end),lt"dist") end

    def around(self, row1=0, rows=None, cols=None):
        rows = rows or self.rows
        def distance(row2):
            return {"row": row2, "dist": self.dist(row1, row2, cols)}
        sorted_rows = sorted(map(distance, rows), key=lambda x: x["dist"])
        return sorted_rows

# function DATA.half(i,rows,  cols,above) --> t,t,row,row,row,n; divides data using 2 far points
#   local A,B,left,right,c,dist,mid,some,project
#   function project(row)    return {row=row, dist=cosine(dist(row,A), dist(row,B), c)} end
#   function dist(row1,row2) return i:dist(row1,row2,cols) end
#   rows = rows or i.rows
#   some = many(rows,the.Sample)
#   A    = above or any(some)
#   B    = i:around(A,some)[(the.Far * #rows)//1].row
#   c    = dist(A,B)
#   left, right = {}, {}
#   for n,tmp in pairs(sort(map(rows, project), lt"dist")) do
#     if   n <= #rows//2 
#     then push(left,  tmp.row); mid = tmp.row
#     else push(right, tmp.row) end end
#   return left, right, A, B, mid, c end

    def half(self, rows=None, cols=None, above=None):
        def dist(row1, row2):
            return self.dist(row1, row2, cols)

        def project(row):
            return {
                "row": row,
                "dist": Misc.cosine(dist(row, A), dist(row, B), c),
            }

        rows = rows or self.rows

        some = Misc.many(rows, 512)
        A = above or Misc.any(some)
        B = self.around(A, some)[int(0.95 * len(rows))]["row"]
        c = dist(A, B)
        left, right = [], []
        mid = None

        for n, tmp in enumerate(
            list(map(project, rows)).sort(key=lambda x: x["dist"])
        ):
            if n <= len(rows) // 2:
                left.append(tmp["row"])
                mid = tmp["row"]
            else:
                right.append(tmp["row"])
        return left, right, A, B, mid, c

# function DATA.cluster(i,  rows,min,cols,above) --> t; returns `rows`, recursively halved
#   local node,left,right,A,B,mid
#   rows = rows or i.rows
#   min  = min or (#rows)^the.min
#   cols = cols or i.cols.x
#   node = {data=i:clone(rows)} --xxx cloning
#   if #rows > 2*min then
#     left, right, node.A, node.B, node.mid = i:half(rows,cols,above)
#     node.left  = i:cluster(left,  min, cols, node.A)
#     node.right = i:cluster(right, min, cols, node.B) end
#   return node end

    def cluster(self, rows=None, min_size=None, cols=None, above=None):
        rows = rows or self.rows
        min_val = min_val or (len(rows)) ** 0.5
        if not cols:
            cols = self.cols.x
        node = {"data": self.clone(rows)}
        if len(rows) > 2 * min_val:
            left, right, node["A"], node["B"], node["mid"], temp = self.half(rows, cols, above)
            node["left"] = self.cluster(left, min_val, cols, node["A"])
            node["right"] = self.cluster(right, min_val, cols, node["B"])
        
        return node

# function DATA.sway(i,  rows,min,cols,above) --> t; returns best half, recursively
#   local node,left,right,A,B,mid
#   rows = rows or i.rows
#   min  = min or (#rows)^the.min
#   cols = cols or i.cols.x
#   node = {data=i:clone(rows)} --xxx cloning
#   if #rows > 2*min then
#     left, right, node.A, node.B, node.mid = i:half(rows,cols,above)
#     if i:better(node.B,node.A) then left,right,node.A,node.B = right,left,node.B,node.A end
#     node.left  = i:sway(left,  min, cols, node.A) end
#   return node end

    def sway(self, rows=None, min=None, cols=None, above=None):
        rows = rows or self.rows
        min = min or len(rows) ** 0.5
        cols = cols or self.cols.x
        node = {"data": self.clone(rows)}

        if len(rows) > 2 * min:
            left, right, node["A"], node["B"], node["min"], _ = self.half(rows, cols, above)
            if self.better(node["B"], node["A"]):
                left, right, node["A"], node["B"] = right, left, node["B"], node["A"]
            node["left"] = self.sway(left, min, cols, node["A"])

        return node
