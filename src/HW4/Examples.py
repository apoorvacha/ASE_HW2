from Sym import Sym
from Num import Num
from Data import *
import Misc
import default

data = Data(default.the["file"])

def test_sym():
    value = ['a', 'a', 'a', 'a', 'b', 'b', 'c']
    sym1 = Sym()
    for x in value:
        sym1.add(x)
    return "a"==sym1.mid() and 1.379 == Misc.rnd(sym1.div())

def test_nums():
    val = Num()
    lst = [1,1,1,1,2,2,3]
    for a in lst:
        val.add(a)
    assert 11/7 == val.mid() and 0.787 == Misc.rnd(val.div())
    assert "test_nums : pass"
    return 11/7 == val.mid() and 0.787 == Misc.rnd(val.div())

def test_the():
    print(str(default.the))
    return True

def test_every():
    Misc.repgrid(default.the["file"])
    return True
