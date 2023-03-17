# function COL(n,s,    col)
#    col = s:find"^[A-Z]" and NUM(n,s) or SYM(n,s) 
#    col.isIgnored  = col.txt:find"X$"
#    col.isKlass    = col.txt:find"!$"
#    col.isGoal     = col.txt:find"[!+-]$"
#    return col end
from Num import *
from Sym import *
import re

class COL:
    def __init__(self, n, s):

        self.col = Num(n, s) if re.match("^[A-Z]",s) else Sym(n, s)
        self.isIgnored = self.col.txt.endswith("X")
        self.isKlass = self.col.txt.endswith("!")
        self.isGoal = self.col.txt[-1] in ["!", "+", "-"]
# import re
# import Num
# import Sym

# class COL:
#      def __init__(self, t, s):
#         self.col = Num(t, s) if s[0].isupper() else Sym(t, s)
#         self.isIgnored = self.col.txt.endswith("X")
#         self.isKlass = self.col.txt.endswith("!")
#         self.isGoal = self.col.txt[-1] in ["!", "+", "-"]
        # self.names = t
        # self.all = []
        # self.x = []
        # self.y = []
        # self.klass = None 

        # for n, s in enumerate(t):
        #     col = Num.Num(n,s) if re.match("^[A-Z]", s) else Sym.Sym(n,s)
        #     self.all.append(col)
        #     if not re.match(".*X$",s):
        #         if re.match("!$",s):
        #             self.klass = col
        #         if re.match('.*\+$',s) or re.match('.*\-$',s) or re.match('.*\!$',s):
        #             self.y.append(col)
        #         else:
        #             self.x.append(col)
    
     
    
