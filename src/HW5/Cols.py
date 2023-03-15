'''
function COLS(ss,     col,cols)
  cols={names=ss, all={},x={},y={}}
  for n,s in pairs(ss) do  
    col = push(cols.all, COL(n,s))
    if not col.isIgnored then
      if col.isKlass then cols.klass = col end
      push(col.isGoal and cols.y or cols.x, col) end end 
  return cols ends
'''
from src.col import Col  # type: ignore


class Cols:
    def __init__(self, ss):
        
        self.names = ss
        self.all = []
        self.x = []
        self.y = []
        for i, val in enumerate(ss):
            col = Col(i, val)
            self.all.append(col)
            if not col.isIgnored:
                if col.isKlass:
                    col.isKlass = col
                if col.isGoal:
                    self.y.append(col)
                else:
                    self.x.append(col)
