# --- ## Examples
# local egs,eg={}
# function eg(key,str, fun) --> nil; register an example.
#   egs[key]=fun
#   help=help..fmt("  -g  %s\t%s\n",key,str) end

# --- eg("crash","show crashing behavior", function()
# ---   return the.some.missing.nested.field end)

# eg("the","show settings",function() oo(the) end)

# eg("sym","check syms", function()
#   local sym=SYM()
#   for _,x in pairs{"a","a","a","a","b","b","c"} do sym:add(x) end
#   return "a"==sym:mid() and 1.379 == rnd(sym:div())end)

# eg("num", "check nums", function()
#   local num=NUM()
#   for _,x in pairs{1,1,1,1,2,2,3} do num:add(x) end
#   return 11/7 == num:mid() and 0.787 == rnd(num:div()) end )

# eg("csv","read from csv", function(n) 
#   n=0;
#   csv(the.file,function(t) n=n+#t end)
#   return n==8*399 end)

# eg("data","read DATA csv", function(     data) 
#   data=DATA(the.file)
#   return #data.rows == 398 and
#          data.cols.y[1].w == -1 and
#          data.cols.x[1].at == 1 and 
#          #data.cols.x==4 end)

# eg("stats","stats from DATA", function(     data) 
#   data=DATA(the.file)
#   for k,cols in pairs({y=data.cols.y,x=data.cols.x}) do
#     print(k,"mid",o(data:stats("mid",cols,2 )))
#     print("", "div",o(data:stats("div",cols,2))) end end)

# main(the,help, egs)