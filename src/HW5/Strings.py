# fmt  = string.format

# -- print to standard error
# function say(...)   io.stderr:write(fmt(...)) end
# function sayln(...) io.stderr:write(fmt(...).."\n") end

# -- Print a nested table (sorted by the keys of the table).
# function oo(t) print(o(t)); return t end
# function o(t,    fun) 
#   if type(t)~="table" then return tostring(t) end
#   function fun (k,v) return fmt(":%s %s",k,o(v)) end 
#   return "{"..table.concat(#t>0  and map(t,o) or sort(kap(t,fun))," ").."}" end