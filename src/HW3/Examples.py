# --- ## Examples
# local egs,eg={}
# function eg(key,str, fun) --> nil; register an example.
#   egs[key]=fun
#   help=help..fmt("  -g  %s\t%s\n",key,str) end

# --- eg("crash","show crashing behavior", function()
# ---   return the.some.missing.nested.field end)

# eg("the","show settings",function() oo(the) end)

# eg("csv","read from csv", function(n) 
#   n=0;
#   csv(the.file,function(t) n=n+#t end)
#   return n==8*399 end)

# eg("data","read DATA csv", function(     data) 
#   data=DATA(the.file)
#   return #data.rows == 398 and
#          data.cols.y[1].w == -1 and
#          data.cols.x[1].at == 1 and 
#          #data.cols.x==4 end)

# eg("stats","stats from DATA", function(     data) 
#   data=DATA(the.file)
#   for k,cols in pairs({y=data.cols.y,x=data.cols.x}) do
#     print(k,"mid",o(data:stats("mid",cols,2 )))
#     print("", "div",o(data:stats("div",cols,2))) end end)

# main(the,help, egs)



# eg("num", "check nums", function()
#   local num=NUM()
#   for _,x in pairs{1,1,1,1,2,2,3} do num:add(x) end
#   return 11/7 == num:mid() and 0.787 == rnd(num:div()) end )
# 
import sys, getopt
# sys.path.insert(0, '/Users/apoorva/Documents/Ase/hw2/ASE_HW2/src')
# import Num, Sym, Misc
from Num import *
from Misc import *
from Sym import *
from Data import *

p = [1,1,1,1,2,2,3]

def test_nums():
    num1 = num()
    for x in p:
     num1.add(x)
    return 11/7 == num1.mid(0) and 0.787 == rnd(num1.div(0))

# eg("sym","check syms", function()
#   local sym=SYM()
#   for _,x in pairs{"a","a","a","a","b","b","c"} do sym:add(x) end
#   return "a"==sym:mid() and 1.379 == rnd(sym:div())end)

value = ['a', 'a', 'a', 'a', 'b', 'b', 'c']

def test_sym():
    sym1 = sym()
    for x in value:
        # print("here")
        sym1.add(x)
    return "a"==sym1.mid(0) and 1.379 == rnd(sym1.div(0))

def test_data():
    path = "../etc/data/auto93.csv"
    data = Data(path)
    
    return  len(data.rows) == 398 and \
            data.cols.y[0].w == -1 and \
            data.cols.x[1].at == 1 and \
            len(data.cols.x) == 4
    
def test_clone():
    path = "../etc/data/auto93.csv"
    data1 = Data(path)
    data2 = data1.clone(data1.rows)
    return  len(data1.rows) == len(data2.rows) and \
            data1.cols.y[1].w == data2.cols.y[1].w and \
            data1.cols.x[1].at == data2.cols.x[1].at and \
            len(data1.cols.x) == len(data2.cols.x)

def test_around():
    path = "../etc/data/auto93.csv"
    data = Data(path)
    for n, t in enumerate(data.around(data.rows[1])):
        if n % 50 == 0:
            print(n, rnd(t["dist"], 2), (t["row"]))
    return True

def test_half():
    path = "../etc/data/auto93.csv"
    data = Data(path)
    left, right, A, B, mid, c = data.half()
    print(len(left), len(right), len(data.rows))
    print(o(A), c)
    print(o(mid))
    print(o(B))
    return True

def test_cluster():
    path = "../etc/data/auto93.csv"
    data = Data(path)
    show(data.cluster(), "mid", data.cols.y, 1)
    return True

def test_optimize():
    path = "../etc/data/auto93.csv"
    data = Data(path)
    show(data.sawy(), "mid", data.cols.y, 1)
    return True