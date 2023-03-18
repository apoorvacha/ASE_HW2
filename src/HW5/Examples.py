# -- ## <a name=egs>Examples</a>
from Num import Num
from Sym import Sym
from Start import the
import Query
from Data import *
import Misc
from pathlib import Path
import os , csv
import Update
import Cluster
# -- Place to store examples.
# local egs = {}
# help = help .. "\nACTIONS:\n"

# -- Used `go` to define an example
# function go(key,xplain,fun)
#   help =  help ..fmt("  -g  %s\t%s\n",key,xplain)
#   egs[1+#egs] = {key=key,fun=fun} end

# -- Disable an example by renaming it `no`. 
# function no(_,__,___) return true end

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



def test_nums():
    val = Num()
    val1 = Num()
    for i in range(1000):
        val.add(Misc.rand())
    for i in range(1000):
        val1.add(Misc.rand()**2)
    print(1,Misc.rnd(val.mid()), Misc.rnd(val.div()))
    print(2,Misc.rnd(val1.mid()), Misc.rnd(val1.div())) 
    return .578 == Misc.rnd(val.mid()) and val.mid()> val1.mid() 


def test_sym():
    value = ['a', 'a', 'a', 'a', 'b', 'b', 'c']
    sym1 = Sym()
    for x in value:
        sym1.add(x)
    return "a"==sym1.mid() and 1.379 == Misc.rnd(sym1.div())

def readCSV(sFilename, fun):
  
    with open(sFilename, mode='r') as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            fun(line)


def test_csv():

    global n
    def fun(t):
        n += len(t)
    root = str(Path(__file__).parent.parent.parent)
    csv_path = os.path.join(root, "etc/data/auto93.csv")
    return csv_content(csv_path) == 8 * 399

def csv_content(src):
    with open(src, mode='r') as file:
        csvFile = csv.reader(file)
        l =0
        for row in csvFile:
            l += len(row)
        return l



#  script_dir = os.path.dirname(__file__)
#     full_path = os.path.join(script_dir, args.file)
#     dataOBJ = DATA()
#     data = dataOBJ.read(full_path)
#     col = data.cols.x[1].col
#     print(col.lo,col.hi, query.mid(col), query.div(col))
#     print(query.stats(data))

def test_data():
    root = str(Path(__file__).parent.parent.parent)
    csv_path = os.path.join(root, "etc/data/auto93.csv")
    # data = Data(csv_path)
    data1 = Data()

    data = data1.read(csv_path)
    col = data.cols.x[1].col
    print(col.lo,col.hi, Query.mid(col), Query.div(col))
    print(Query.stats(data))




# go("clone","replicate structure of a DATA",function(    data1,data2)
#   data1=DATA.read(the.file)
#   data2=DATA.clone(data1,data1.rows) 
#   oo(stats(data1))
#   oo(stats(data2)) end)

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

# go("half","divide data in halg", function(   data,l,r)
#   data = DATA.read(the.file)
#   local left,right,A,B,c = half(data) 
#   print(#left,#right)
#   l,r = DATA.clone(data,left), DATA.clone(data,right)
#   print("l",o(stats(l)))
#   print("r",o(stats(r))) end)

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

def test_cliffs():
    if Misc.cliffs_delta([8, 7, 6, 2, 5, 8, 7, 3], [8, 7, 6, 2, 5, 8, 7, 3]):
        return False
    if not Misc.cliffs_delta([8, 7, 6, 2, 5, 8, 7, 3], [9, 9, 7, 8, 10, 9, 6]):
        return False

    t1, t2 = [], []
    for i in range(1000):
        t1.append(Misc.rand())
        t2.append(math.sqrt(Misc.rand()))
    if Misc.cliffs_delta(t1, t1):
        return False
    if not Misc.cliffs_delta(t1, t2):
        return False
    diff, j = False, 1.0
    while not diff:
        t3 = list(map(lambda x: x * j,t1))
        diff = Misc.cliffs_delta(t1, t3)
        print(">", Misc.rnd(j), diff)
        j *= 1.025
    
    return True

def test_dist():
    root = str(Path(__file__).parent.parent.parent)
    csv_path = os.path.join(root, "etc/data/auto93.csv")
    data1 = Data()

    data = data1.read(csv_path)
    num = Num()
    for row in data.rows:
        Update.add(num, Query.dist(data, row, data.rows[1]))
    # print({"lo": num.lo, "hi": num.hi, "mid": rnd(mid(num)), "div": rnd(num)})
    print({"lo": num.lo, "hi": num.hi, "mid": Misc.rnd(Query.mid(num)), "div": Misc.rnd(num.n)})
    return True

def test_tree():
    root = str(Path(__file__).parent.parent.parent)
    csv_path = os.path.join(root, "etc/data/auto93.csv")
    data1 = Data()

    data = data1.read(csv_path)
    Cluster.show_tree(Cluster.tree(data))