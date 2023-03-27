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

def add(i, x):
    i.n += 1
    d = x - i.mu
    i.mu = i.mu + d/i.n
    i.m2 = i.m2 + d * (x - i.mu)
    i.sd = 0 if i.n < 2 else (i.m2 / i.n - 1) ** 0.5

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