import random
import Misc
from Num import Num

def test_ok():
    print(random.seed(1))

def test_sample():
    for i in range(10):
        print("", "".join(Misc.samples(["a", "b", "c", "d", "e"])))

def test_num():
    n = Num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(n.n, n.mu, n.sd)

def test_gaussian():
    t = []
    for i in range(10 ** 4 + 1):
        t.append(Misc.gaussian(10, 2))
    n = Num(t)
    print(n.n, n.mu, n.sd)

def test_bootstrap():
    a, b = [], []
    for i in range(100):
        a.append(Misc.gaussian(10, 1))
    print("","mu","sd","cliffs","boot","both")
    print("","--","--","------","----","----")
    mu = 10.0
    while mu <= 11.0:
        b.clear()
        for i in range(100):
            b.append(Misc.gaussian(mu, 1))
        cl = Misc.cliffsDelta(a, b)
        bs = Misc.bootstrap(a, b)
        print("", mu, 1, cl, bs, cl and bs)
        mu += 0.1

def test_basic():
        print("\t\ttruee", Misc.bootstrap([8, 7, 6, 2, 5, 8, 7, 3], [8, 7, 6, 2, 5, 8, 7, 3]),
                        Misc.cliffsDelta([8, 7, 6, 2, 5, 8, 7, 3], [8, 7, 6, 2, 5, 8, 7, 3]))
        print("\t\tfalse", Misc.bootstrap([8, 7, 6, 2, 5, 8, 7, 3], [9, 9, 7, 8, 10, 9, 6]),
                        Misc.cliffsDelta([8, 7, 6, 2, 5, 8, 7, 3], [9, 9, 7, 8, 10, 9, 6]))
        print("\t\tfalse", Misc.bootstrap([0.34, 0.49, 0.51, 0.6, 0.34, 0.49, 0.51, 0.6], [0.6, 0.7, 0.8, 0.9, 0.6, 0.7, 0.8, 0.9]),
                        Misc.cliffsDelta([0.34, 0.49, 0.51, 0.6, 0.34, 0.49, 0.51, 0.6], [0.6, 0.7, 0.8, 0.9, 0.6, 0.7, 0.8, 0.9]))


def test_pre():
    print("\neg3")
    d = 1
    for i in range(10):
        t1, t2 = [], []
        for j in range(32):
            t1.append(Misc.gaussian(10, 1))
            t2.append(Misc.gaussian(d * 10, 1))
        print("\t", d, "true" if d < 1.1 else "false", Misc.bootstrap(t1, t2), Misc.bootstrap(t1, t1))
        d += 0.05

def test_five():
    rx_test = [Misc.RX([0.34,0.49,0.51,0.6,.34,.49,.51,.6],"rx1"), 
                     Misc.RX([0.6,0.7,0.8,0.9,.6,.7,.8,.9],"rx2"), 
                     Misc.RX([0.15,0.25,0.4,0.35,0.15,0.25,0.4,0.35],"rx3"), 
                     Misc.RX([0.6,0.7,0.8,0.9,0.6,0.7,0.8,0.9],"rx4"), 
                     Misc.RX([0.1,0.2,0.3,0.4,0.1,0.2,0.3,0.4],"rx5")]
    sk = Misc.scottKnot(rx_test)
    tiles_sk = Misc.tiles(sk)
    for rx in tiles_sk:
        print(rx["name"], rx["rank"], rx["show"])

def test_six():
    rx_test = [Misc.RX([101,100,99,101,99.5,101,100,99,101,99.5],"rx1"), 
                     Misc.RX([101,100,99,101,100,101,100,99,101,100],"rx2"), 
                     Misc.RX([101,100,99.5,101,99,101,100,99.5,101,99],"rx3"), 
                     Misc.RX([101,100,99,101,100,101,100,99,101,100],"rx4")]
    sk = Misc.scottKnot(rx_test)
    tiles_sk = Misc.tiles(sk)
    for rx in tiles_sk:
        print(rx["name"], rx["rank"], rx["show"])

def test_tiles():
    rxs,a,b,c,d,e,f,g,h,j,k=[],[],[],[],[],[],[],[],[],[],[]
    for i in range(1000):
        a.append(Misc.gaussian(10,1))
    for i in range(1000):
        b.append(Misc.gaussian(10.1,1))
    for i in range(1000):
        c.append(Misc.gaussian(20,1))
    for i in range(1000):
        d.append(Misc.gaussian(30,1))
    for i in range(1000):
        e.append(Misc.gaussian(30.1,1))
    for i in range(1000):
        f.append(Misc.gaussian(10,1))
    for i in range(1000):
        g.append(Misc.gaussian(10,1))
    for i in range(1000):
        h.append(Misc.gaussian(40,1))
    for i in range(1000):
        j.append(Misc.gaussian(40,3))
    for i in range(1000):
        k.append(Misc.gaussian(10,1))
    for k, v in enumerate([a, b, c, d, e, f, g, h, j, k]):
        rxs.append(Misc.RX(v, "rx" + str(k)))
    rxs.sort(key=lambda a: Misc.mid(a))
    for rx in Misc.tiles(rxs):
        print("",rx["name"],rx["show"])

def test_sk():
    rxs,a,b,c,d,e,f,g,h,j,k=[],[],[],[],[],[],[],[],[],[],[]
    for i in range(1000):
        a.append(Misc.gaussian(10,1))
    for i in range(1000):
        b.append(Misc.gaussian(10.1,1))
    for i in range(1000):
        c.append(Misc.gaussian(20,1))
    for i in range(1000):
        d.append(Misc.gaussian(30,1))
    for i in range(1000):
        e.append(Misc.gaussian(30.1,1))
    for i in range(1000):
        f.append(Misc.gaussian(10,1))
    for i in range(1000):
        g.append(Misc.gaussian(10,1))
    for i in range(1000):
        h.append(Misc.gaussian(40,1))
    for i in range(1000):
        j.append(Misc.gaussian(40,3))
    for i in range(1000):
        k.append(Misc.gaussian(10,1))
    for k, v in enumerate([a, b, c, d, e, f, g, h, j, k]):
        rxs.append(Misc.RX(v, "rx" + str(k)))
    for rx in Misc.tiles(Misc.scottKnot(rxs)):
        print("",rx["rank"],rx["name"],rx["show"])