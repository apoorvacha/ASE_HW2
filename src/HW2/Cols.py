# -- ### COLS
# -- Factory for managing a set of NUMs or SYMs
# function COLS.new(i,t,     col,cols) --> COLS; generate NUMs and SYMs from column names
#   i.names, i.all, i.x, i.y, i.klass = t, {}, {}, {}
#   for n,s in pairs(t) do  -- like PYTHONS's for n,s in enumerate(t) do..
#     col = s:find"^[A-Z]+" and NUM(n,s) or SYM(n,s)
#     push(i.all, col)
#     if not s:find"X$" then
#       if s:find"!$" then i.klass = col end
#       push(s:find"[!+-]$" and i.y or i.x, col) end end end

# function COLS.add(i,row) --> nil; update the (not skipped) columns with details from `row`
#   for _,t in pairs({i.x,i.y}) do 
#     for _,col in pairs(t) do
#       col:add(row.cells[col.at]) end end end

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
