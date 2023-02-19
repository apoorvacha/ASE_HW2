# go("the","show options",function() oo(the) end)

# go("rand","demo random number generation", function(     t,u)
#   Seed=1; t={}; for i=1,1000 do push(t,rint(100)) end
#   Seed=1; u={}; for i=1,1000 do push(u,rint(100)) end
#   for k,v in pairs(t) do assert(v==u[k]) end end)

# go("some","demo of reservoir sampling", function(     num1)
#   the.Max = 32
#   num1 = NUM()
#   for i=1,10000 do add(num1,i) end
#   oo(has(num1)) end)



# go("clone","replicate structure of a DATA",function(    data1,data2)
#   data1=DATA.read(the.file)
#   data2=DATA.clone(data1,data1.rows) 
#   oo(stats(data1))
#   oo(stats(data2)) end)


# go("cliffs","stats tests", function(   t1,t2,t3)
#   assert(false == cliffsDelta( {8,7,6,2,5,8,7,3},{8,7,6,2,5,8,7,3}),"1")
#   assert(true  == cliffsDelta( {8,7,6,2,5,8,7,3}, {9,9,7,8,10,9,6}),"2") 
#   t1,t2={},{}
#   for i=1,1000 do push(t1,rand()) end --rand()/10) end
#   for i=1,1000 do push(t2,rand()^.5) end --rand()*10) end
#   assert(false == cliffsDelta(t1,t1),"3") 
#   assert(true  == cliffsDelta(t1,t2),"4") 
#   local diff,j=false,1.0
#   while not diff  do
#     t3=map(t1,function(x) return x*j end)
#     diff=cliffsDelta(t1,t3)
#     print(">",rnd(j),diff) 
#     j=j*1.025 end end)

# go("dist","distance test", function(    data,num)
#   data = DATA.read(the.file)
#   num  = NUM()
#   for _,row in pairs(data.rows) do
#     add(num,dist(data, row, data.rows[1])) end
#   oo{lo=num.lo, hi=num.hi, mid=rnd(mid(num)), div=rnd(div(num))} end)

# go("half","divide data in halg", function(   data,l,r)
#   data = DATA.read(the.file)
#   local left,right,A,B,c = half(data) 
#   print(#left,#right)
#   l,r = DATA.clone(data,left), DATA.clone(data,right)
#   print("l",o(stats(l)))
#   print("r",o(stats(r))) end)
 
# go("tree","make snd show tree of clusters", function(   data,l,r)
#   showTree(tree(DATA.read(the.file))) end)

# go("sway","optimizing", function(    data,best,rest)
#   data = DATA.read(the.file)
#   best,rest = sway(data)
#   print("\nall ", o(stats(data))) 
#   print("    ",   o(stats(data,div))) 
#   print("\nbest", o(stats(best))) 
#   print("    ",   o(stats(best,div))) 
#   print("\nrest", o(stats(rest))) 
#   print("    ",   o(stats(rest,div))) 
#   print("\nall ~= best?", o(diffs(best.cols.y, data.cols.y)))
#   print("best ~= rest?", o(diffs(best.cols.y, rest.cols.y))) end)

# go("bins", "find deltas between best and rest", function(    data,best,rest, b4)
#   data = DATA.read(the.file)
#   best,rest = sway(data)
#   print("all","","","",o{best=#best.rows, rest=#rest.rows})
#   for k,t in pairs(bins(data.cols.x,{best=best.rows, rest=rest.rows})) do
#     for _,range in pairs(t) do
#       if range.txt ~= b4 then print"" end
#       b4 = range.txt
#       print(range.txt,range.lo,range.hi,
#            rnd(value(range.y.has, #best.rows,#rest.rows,"best")), 
#            o(range.y.has)) end end end)


from Num import Num
from Sym import Sym
from Start import the
from Misc import *
from pathlib import Path
from Data import *
import os 

# go("nums","demo of NUM", function(     num1,num2)
#   num1,num2 = NUM(), NUM()
#   for i=1,10000 do add(num1, rand()) end
#   for i=1,10000 do add(num2, rand()^2) end
#   print(1,rnd(mid(num1)), rnd(div(num1)))
#   print(2,rnd(mid(num2)), rnd(div(num2))) 
#   return .5 == rnd(mid(num1)) and mid(num1)> mid(num2) end)
def test_nums():
    val = Num()
    val1 = Num()
    for i in range(1000):
        val.add(rand())
    for i in range(1000):
        val1.add(rand()**2)
    print(1,rnd(val.mid()), rnd(val.div()))
    print(2,rnd(val1.mid()), rnd(val1.div())) 
    return .578 == rnd(val.mid()) and val.mid()> val1.mid() 
    
# go("syms","demo SYMS", function(    sym)
#   sym=adds(SYM(), {"a","a","a","a","b","b","c"})
#   print (mid(sym), rnd(div(sym))) 
#   return 1.38 == rnd(div(sym)) end)

def test_sym():
    value = ['a', 'a', 'a', 'a', 'b', 'b', 'c']
    sym1 = Sym()
    for x in value:
        sym1.add(x)
    return "a"==sym1.mid() and 1.379 == rnd(sym1.div())


def test_csv():
    root = str(Path(__file__).parent.parent.parent)
    csv_path = os.path.join(root, "etc/data/auto93.csv")
    data = Data(csv_path)
    return data.count == 8*399

def test_data():
    root = str(Path(__file__).parent.parent.parent)
    csv_path = os.path.join(root, "etc/data/auto93.csv")
    data = Data(csv_path)
    return  len(data.rows) == 398 and \
            data.cols.y[0].w == -1 and \
            data.cols.x[1].at == 1 and \
            len(data.cols.x) == 4



# go("csv","reading csv files", function(     n)
#   n=0; csv(the.file, function(t) n=n+#t end) 
#   return 3192 == n end)

# go("data", "showing data sets", function(    data,col) 
#   data=DATA.read(the.file)
#   col=data.cols.x[1]
#   print(col.lo,col.hi, mid(col),div(col))
#   oo(stats(data)) end)

def test_clone():
    root = str(Path(__file__).parent.parent.parent)
    csv_path = os.path.join(root, "etc/data/auto93.csv")
    data1 = Data(csv_path)
    data2 = data1.clone(data1.rows)
    return  len(data1.rows) == len(data2.rows) and \
            data1.cols.y[1].w == data2.cols.y[1].w and \
            data1.cols.x[1].at == data2.cols.x[1].at and \
            len(data1.cols.x) == len(data2.cols.x)

def test_the():
    print(str(the))
    return True

def test_half():
    root = str(Path(__file__).parent.parent.parent)
    csv_path = os.path.join(root, "etc/data/auto93.csv")
    data = Data(csv_path)

    left, right, A, B, mid, c = data.half()
    print(len(left), len(right), len(data.rows))
    print(o(A), c)
    print(o(mid))
    print(o(B))
    return True