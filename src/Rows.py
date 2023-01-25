# -- ### ROW
# -- Store one record.
# function ROW.new(i,t) i.cells=t; end --> ROW; 

class Rows:
    def __init__(self, t):
        self.cells = t
