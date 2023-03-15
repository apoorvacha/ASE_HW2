# function COL(n,s,    col)
#    col = s:find"^[A-Z]" and NUM(n,s) or SYM(n,s) 
#    col.isIgnored  = col.txt:find"X$"
#    col.isKlass    = col.txt:find"!$"
#    col.isGoal     = col.txt:find"[!+-]$"
#    return col end