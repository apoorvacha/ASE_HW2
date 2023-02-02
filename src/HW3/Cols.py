class Cols:
    def __init__(self, t, col, cols):
        self.names = t
        self.all = {}
        self.x = {}
        self.y = {}
        self.klass = None #Doubt, google and confirm

        for n, s in enumerate(t):
            col = Num(n,s) if re.match("^[A-Z]",s) else Sym(n,s)
            #push(i.all, col) What is push??
            if not re.match("X$"):
                #push(s:find"[!+-]$" and i.y or i.x, col) end end end  Same as 27
    
    def add(self, row):
        for _, t in zip(self.x, self.y):
            for _, col in enumerate(t):
                #col:add(row.cells[col.at]) end end end
