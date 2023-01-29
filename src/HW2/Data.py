# function DATA.new(i,src,     fun) --> DATA; A container of `i.rows`, to be summarized in `i.cols`
#   i.rows, i.cols = {}, nil
#   fun = function(x) i:add(x) end
#   if type(src) == "string" then csv(src,fun)  -- load from a csv file on disk
#                            else map(src or {}, fun)  --  load from a list
#                            end end
  
# function DATA.add(i,t) --> nil; add a new row, update column headers
#   if   i.cols          --] true if we have already seen the column names
#   then t = t.cells and t or ROW(t) -- ensure is a ROW, reusing old rows in the are passed in
#        -- t =ROW(t.cells and t.cells or t) -- make a new ROW
#        push(i.rows, t) -- add new data to "i.rows"
#        i.cols:add(t)  -- update the summary information in "ic.ols"
#   else i.cols=COLS(t)  end end --  here, we create "i.cols" from the first row

# function DATA.clone(i,  init,     data) --> DATA; return a DATA with same structure as `ii. 
#   data=DATA({i.cols.names})
#   map(init or {}, function(x) data:add(x) end)
#   return data end

# function DATA.stats(i,  what,cols,nPlaces) --> t; reports mid or div of cols (defaults to i.cols.y)
#   local fun
#   function fun(k,col) return col:rnd(getmetatable(col)[what or "mid"](col),nPlaces),col.txt end
#   return kap(cols or i.cols.y, fun) end