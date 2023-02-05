from Num import Num
from Sym import Sym
from Start import the
from Misc import *


def test_nums():
    val = Num()
    lst = [1,1,1,1,2,2,3]
    for a in lst:
        val.add(a)
    assert 11/7 == val.mid() and 0.787 == rnd(val.div())
    assert "test_nums : pass"
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