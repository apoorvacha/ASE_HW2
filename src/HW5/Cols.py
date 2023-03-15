import re
from Num import *
from Sym import *

class Cols:
     def __init__(self, t):
        self.names = t
        self.all = []
        self.x = []
        self.y = []
        self.klass = None 

        for n, s in enumerate(t):
            print("here",s)
            col = Num(n,s) if re.match("^[A-Z]", s) else Sym(n,s)
            self.all.append(col)
            if not re.match(".*X$",s):
                if re.match("!$",s):
                    self.klass = col
                if re.match('.*\+$',s) or re.match('.*\-$',s) or re.match('.*\!$',s):
                    self.y.append(col)
                else:
                    self.x.append(col)
    
     def add(self, row):
        lst = [self.x,self.y]
        for _, t in enumerate(lst):
            for _, col in enumerate(t):
                col.add(row.cells[col.at])
    

# function COLS(ss,     col,cols)
#   cols={names=ss, all={},x={},y={}}
#   for n,s in pairs(ss) do  
#     col = push(cols.all, COL(n,s))
#     if not col.isIgnored then
#       if col.isKlass then cols.klass = col end
#       push(col.isGoal and cols.y or cols.x, col) end end 
#   return cols end