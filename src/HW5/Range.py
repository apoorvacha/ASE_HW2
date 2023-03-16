# -- Create a RANGE  that tracks the y dependent values seen in 
# -- the range `lo` to `hi` some independent variable in column number `at` whose name is `txt`. 
# -- Note that the way this is used (in the `bins` function, below)
# -- for  symbolic columns, `lo` is always the same as `hi`.
# function RANGE(at,txt,lo,hi) 
#   return {at=at,txt=txt,lo=lo,hi=lo or hi or lo,y=SYM()} end

from Sym import *


class RANGE:
    def __init__(self, at=None, txt=None, lo=None, hi=None):
        
        self.at = at
        self.txt = txt
        self.lo = lo
        self.hi = lo if lo else hi if hi else lo
        self.y = Sym()