from Num import Num
from Sym import Sym
from Start import the
from Misc import * 
from pathlib import Path
import os 


def test_nums():
    val = Num()
    lst = [1,1,1,1,2,2,3]
    for a in lst:
        val.add(a)
    assert 11/7 == val.mid() and 0.787 == Misc.rnd(val.div())
    assert "test_nums : pass"
    return 11/7 == val.mid() and 0.787 == Misc.rnd(val.div())
    
def test_sym():
    value = ['a', 'a', 'a', 'a', 'b', 'b', 'c']
    sym1 = Sym()
    for x in value:
        sym1.add(x)
    return "a"==sym1.mid() and 1.379 == Misc.rnd(sym1.div())

def test_the():
    print(str(the))
    return True

def test_every():
    root = str(Path(__file__).parent.parent.parent)
    csv_path = os.path.join(root, "etc/data/repgrid1.csv")
    repgrid(csv_path)

