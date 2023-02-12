import math
from Start import the
def rnd(n, nPlaces=3):
    mult = 10**(nPlaces or 3)
    return math.floor(n * mult + 0.5) / mult

# oo, rand , generate, 

def rand(lo=0,hi=1):
    seed1 = the["seed"]
    seed1 = (16807*seed1) % 2147483647
    return lo+(hi-lo) * seed1/2147483647