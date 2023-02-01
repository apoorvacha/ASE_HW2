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

import csv
from typing import List
import Cols
import Rows

# reading the CSV file
def csv_content(src):
    res = []
    with open(src, mode='r') as file:
        csvFile = csv.reader(file)
        res.append(csvFile)

    return res

class Data:

    def __init__(self, src):
        self.rows = []
        self.cols = None

        if type(src) == str:
            csv_list = csv_content(src)
            for row in csv_list:
                row_cont = []
                for val in row:
                    row_cont.append(val.strip())
                self.add(row_cont)

        elif type(src) == List[str]:  # else we were passed the columns as a string
            self.add(src)

    def add(self, t: list[str]):

        if (self.cols):
            row = Rows.Rows(t)
            self.rows.append(row)
            self.cols.add(row)
        else:
            self.cols = Cols.Cols(t)

    def clone(self):
        data = Data({self.cols.names})
        for row in self.rows:
            data.add(row)
        return data
    
    def stats(self,what,cols,nPlaces):
        return None
