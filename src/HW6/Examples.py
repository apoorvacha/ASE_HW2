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