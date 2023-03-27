from Num import *
from Misc import *

def test_num():
    n = Num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(n.n, n.mu, n.sd)

def test_gaussian():
    t = []
    for i in range(10 ** 4 + 1):
        t.append(Misc.gaussian(10, 2))