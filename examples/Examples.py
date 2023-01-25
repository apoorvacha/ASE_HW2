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
sys.path.insert(0, '/Users/apoorva/Documents/Ase/hw2/ASE_HW2/src')
# from src import Num, Sym, Misc
from Num import *
from Misc import *
from Sym import *

p = [1,1,1,1,2,2,3]

def test_nums():
    num1 = num()
    for x in p:
     num1.add(x)
    return 11/7 == num1.mid(0) and 0.787 == rnd(num1.div(0))

value = ['a', 'a', 'a', 'a', 'b', 'b', 'c']

def test_sym():
    sym1 = sym()
    for x in value:
        # print("here")
        sym1.add(x)
    return "a"==sym1.mid(0) and 1.379 == rnd(sym1.div(0))
