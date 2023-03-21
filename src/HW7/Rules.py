import re
from Num import *
from Sym import *
from Col import *

class Rules:
    def __init__(self,ranges,maxSize):
        self.t = []
        for _,range in enumerate(ranges):
            self.t[range.txt] = self.t[range.txt] or []
            push(self.t[range.txt],[range.lo,range.hi,range.at])
        self.prune(self.t,maxSize)
    
    def prune(rule,maxSize):
        n = 0
        for txt, ranges in enumerate(rule):
            n+=1
            if len(ranges) == maxSize[txt]:
                n+=1
                rule[txt] = None
        if n>0:
             return rule
                
    
