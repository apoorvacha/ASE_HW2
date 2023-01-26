def csv(path):
    pass

class Data:
    def __init__(self, t):
        self.rows, self.cols = [], None
        
        def fun(x):
            self.add(x)
        
        if type(src) == "str":
            csv(src, fun())
        else:
            if src:
                #map(src or {}, fun) doubt
    
    def add(self, t):
        if self.cols:
            if t:
                t = t.cells
            else:
                t = Rows(t)

            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = Cols(t)

    def clone(self, init, data):
        data = Data({self.cols.names})
        for row in self.rows:
            data.add(row)
        return data

    def stats(self, what, cols, nPlaces):
        pass
