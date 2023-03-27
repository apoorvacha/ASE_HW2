import math
import random
from Misc import *
from Num import Num
import argparse

def erf(x):
    a1 =  0.254829592
    a2 = -0.284496736
    a3 =  1.421413741
    a4 = -1.453152027
    a5 =  1.061405429
    p  =  0.3275911
    sign = 1
    if x < 0:
        sign = -1
    x = abs(x)
    t = 1 / (1 + (p * x))
    y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * math.exp(-x * x)
    return sign * y

def gaussian(mu = 0, sd = 1):
    sq = math.sqrt
    pi = math.pi
    log = math.log
    cos = math.cos
    r = random.random
    return mu + sd * sq(-2 * log(r())) * cos(2 * pi * r())

def samples(t, n = None):
    u = []
    for i in range(n or len(t)):
        u.append(random.choice(t))
    return u

def cliffsDelta(ns1, ns2):
    n, gt, lt = 0, 0, 0
    if len(ns1) > 128: ns1 = samples(ns1, 128)
    if len(ns2) > 128: ns2 = samples(ns2, 128)
    for x in ns1:
        for y in ns2:
            n += 1
            if x > y: gt += 1
            if x < y: lt += 1
    return abs(lt - gt) / n <= args.cliff

def add(i, x):
    i.n += 1
    d = x - i.mu
    i.mu += d / i.n
    i.m2 += d * (x - i.mu)
    i.sd = 0 if i.n < 2 else math.sqrt(i.m2 / (i.n - 1))

def delta(i, other):
    e, y, z = 1E-32, i, other
    return abs(y.mu - z.mu) / (math.sqrt(e + y.sd ** 2 / y.n + z.sd ** 2 / z.n))

def bootstrap(y0, z0):
    x, y, z, yhat, zhat = Num(), Num(), Num(), [], []
    for y1 in y0:
        add(x, y1)
        add(y, y1)
    for z1 in z0:
        add(x, z1)
        add(z, z1)
    xmu, ymu, zmu = x.mu, y.mu, z.mu
    for y1 in y0: yhat.append(y1 - ymu + xmu)
    for z1 in z0: zhat.append(z1 - zmu + xmu)
    tobs = delta(y, z)
    n = 0
    for i in range(args.bootstrap):
        if (delta(Num(samples(yhat)), Num(samples(zhat))) > tobs):
            n += 1
    return n / args.bootstrap >= args.conf

args, egs = None, {}

def eg(key, string, fun):
    global egs
    global help
    egs[key] = fun

def getCliArgs():
    global args
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--bootstrap", type=int, default = 512, required=False)
    parser.add_argument("--conf", type=float, default = 0.05, required=False)
    parser.add_argument("--cliff", type=float, default = 0.4, required=False)
    parser.add_argument("--cohen", type=float, default = 0.35, required=False)
    parser.add_argument("--Fmt", type=str, default = "%6.2f", required=False)
    parser.add_argument("--width", type=int, default = 40, required=False)

    args = parser.parse_args()