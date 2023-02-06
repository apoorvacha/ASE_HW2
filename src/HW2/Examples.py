from Num import Num
from Sym import Sym
from start import the
from Misc import *
from Data import Data
from pathlib import Path
import os 

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
    root = str(Path(__file__).parent.parent.parent)
    csv_path = os.path.join(root, "etc/data/auto93.csv")
    data = Data(csv_path)
    return data.count == 8*399

def test_data():
    # path = "../etc/data/auto93.csv"
    # data = Data("/Users/apoorva/Documents/ASE_HW2/etc/data/auto93.csv")
    root = str(Path(__file__).parent.parent.parent)
    csv_path = os.path.join(root, "etc/data/auto93.csv")
    data = Data(csv_path)
    return  len(data.rows) == 398 and \
            data.cols.y[0].w == -1 and \
            data.cols.x[1].at == 1 and \
            len(data.cols.x) == 4

# def test


# eg("sym","check syms", function()
#   local sym=SYM()
#   for _,x in pairs{"a","a","a","a","b","b","c"} do sym:add(x) end
#   return "a"==sym:mid() and 1.379 == rnd(sym:div())end)


