# function COL(n,s,    col)
#    col = s:find"^[A-Z]" and NUM(n,s) or SYM(n,s) 
#    col.isIgnored  = col.txt:find"X$"
#    col.isKlass    = col.txt:find"!$"
#    col.isGoal     = col.txt:find"[!+-]$"
#    return col end
from Num import *
from Sym import *
import re

class Col:
    def __init__(self, n, s):

        self.col = Num(n, s) if re.match("^[A-Z]",s) else Sym(n, s)
        self.isIgnored = self.col.txt.endswith("X")
        self.isKlass = self.col.txt.endswith("!")
        self.isGoal = self.col.txt[-1] in ["!", "+", "-"]