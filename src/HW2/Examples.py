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

from Num import Num
from Sym import Sym
from start import the
from Misc import *
from Data import Data

def test_nums():
    val = Num()
    lst = [1,1,1,1,2,2,3]
    for a in lst:
        val.add(a)
    return 11/7 == val.mid() and 0.787 == rnd(val.div())
    
def test_sym():
    value = ['a', 'a', 'a', 'a', 'b', 'b', 'c']
    sym1 = Sym()
    for x in value:
        sym1.add(x)
    return "a"==sym1.mid() and 1.379 == rnd(sym1.div())

def test_the():
    print(str(the))
    return True

def test_csv():
    data = Data("/Users/vasuagrawal/Downloads/ASE_HW2-main/etc/data/auto93.csv")
    return data.count == 8*399

def test_data():
    # path = "../etc/data/auto93.csv"
    data = Data("/Users/vasuagrawal/Downloads/ASE_HW2-main/etc/data/auto93.csv")
    
    return  len(data.rows) == 398 and \
            data.cols.y[0].w == -1 and \
            data.cols.x[1].at == 1 and \
            len(data.cols.x) == 4

# def test


# eg("sym","check syms", function()
#   local sym=SYM()
#   for _,x in pairs{"a","a","a","a","b","b","c"} do sym:add(x) end
#   return "a"==sym:mid() and 1.379 == rnd(sym:div())end)


