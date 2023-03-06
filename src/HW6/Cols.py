import re
from Num import *
from Sym import *
from Col import *

class Cols:
     def __init__(self,ss):
        self.names = ss
        self.all = []
        self.x = []
        self.y = []
        self.klass = None

        for n, s in enumerate(ss):
            col = push(self.all,Col(n,s))
            if not col.isIgnored and col.isKlass:
                self.klass = col
            if not col.isIgnored:
                temp = self.y if col.isGoal else self.x
                push(temp,col)
                
    
