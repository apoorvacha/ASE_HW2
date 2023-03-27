import argparse
import math
import random

def erf(x):
    a1 =  0.254829592
    a2 = -0.284496736
    a3 =  1.421413741
    a4 = -1.453152027
    a5 =  1.061405429
    p  =  0.3275911

    sign = 1
    if x < 0:
        sign -= 1
    x = abs(x)
    t = 1 / (1 + p*x)
    y = 1 - (((((a5*t + a4)*t) + a3)*t + a2)*t + a1)*t*math.exp(-x*x)

    return sign * y

def gaussian(mu = 0, sd = 1):
    sq, pi, log, cos, r = math.sqrt, math.pi, math.log, math.cos, random.random
    return mu + sd * sq(-2*log(r())) * cos(2*pi*r())

def samples(t, n = None):
    u = []
    for i in range(n or len(t)):
        u.append(random.choice(t))
    return u

def cliffsDelta(ns1, ns2):
    n, gt, lt = 0, 0, 0
    if len(ns1) > 128: ns1 = samples(ns1, 128)
    if len(ns2) > 128: ns2 = samples(ns2, 128)
    for i in ns1:
        for j in ns2:
            n += 1
            if i > j: gt += 1
            if i < j: lt += 1
    return abs(lt - gt) / n <= args.cliff

def add(i, x):
    i.n += 1
    d = x - i.mu
    i.mu = i.mu + d/i.n
    i.m2 = i.m2 + d * (x - i.mu)
    i.sd = 0 if i.n < 2 else (i.m2 / i.n - 1) ** 0.5

def delta(i, other):
    e, y, z = 1E-32, i, other
    return abs(y.mu - z.mu) / ((e + y.sd ** 2 / y.n + z.sd ** 2 / z.n) ** 0.5)

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

args = None
egs = {}

def eg(key, string, fun):
    global egs
    global help
    egs[key] = fun