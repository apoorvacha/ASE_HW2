from Cols import COLS
import Misc 
import random

def row(data, t):
  
    if data.cols:
        data.rows.append(t)
        for cols in [data.cols.x, data.cols.y]:
            for col in cols:
                add(col.col, t[col.col.at])
    else:
        data.cols = COLS(t)
    return data

"""
To check if an object has an attribute in Python, you can use the hasattr function. 
The hasattr function returns a Boolean value indicating whether the object has the specified attribute. 
If the attribute exists, hasattr returns True, otherwise it returns False.
"""
def add(col, x, n = 0):

    if x != "?":
        n = 1
        col.n += n # Source of variable 'n'
        if hasattr(col, "isSym") and col.isSym:
            col.has[x] = n + (col.has.get(x, 0))
            if col.has[x] > col.most:
                col.most = col.has[x]
                col.mode = x
        else:
            #Change x to float value
            x = float(x)
            col.lo = min(x, col.lo)
            col.hi = max(x, col.hi)
            all = len(col.has)
            if all <512:
                pos = all + 1
            elif random.random() < 512 / col.n:
                pos = Misc.rint(1, all)
            else:
                pos = None
            if pos:
                #check if col is an instance of sym or num
                if isinstance(col.has, dict):
                    col.has[pos] = x
                else:
                    col.has.append(x)
                col.ok = False
    
def extend(range, n, s):
  
    range.lo = min(n, range.lo)
    range.hi = max(n, range.hi)
    add(range.y, s)