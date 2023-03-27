from Num import *
from Misc import *

def test_num():
    n = Num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(n.n, n.mu, n.sd)

def test_gaussian():
    t = []
    for i in range(10 ** 4 + 1):
        t.append(Misc.gaussian(10, 2))

def test_bootstrap():
    a, b = [], []
    for i in range(100):
        a.append(gaussian(10, 1))
    print("","mu","sd","cliffs","boot","both")
    print("","--","--","------","----","----")
    mu = 10.0
    while mu <= 11.0:
        b.clear()
        for i in range(100):
            b.append(gaussian(mu, 1))
        cl = cliffsDelta(a, b)
        bs = bootstrap(a, b)
        print("", mu, 1, cl, bs, cl and bs)
        mu += 0.1