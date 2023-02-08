import csv
from typing import List
import Num
import Cols 
import Rows
import Misc

# reading the CSV file
def csv_content(src):
    res = []
    with open(src, mode='r') as file:
        csvFile = csv.reader(file)
        for row in csvFile:
            res.append(row)
    return res

class Data:

    def __init__(self, src):
        self.rows = []
        self.cols = None
        self.count = 0

        if type(src) == str:
            csv_list = csv_content(src)
            for line,row in enumerate(csv_list):
                row_cont = []
                for oth_line,val in enumerate(row):
                    row_cont.append(val.strip())
                    self.count+=1
                self.add(row_cont)

        else:
            if (type(src)) == List[str]:
                self.add(src)


    def add(self, t: list[str]):

        if (self.cols):
            row = Rows.Rows(t)
            self.rows.append(row)
            self.cols.add(row)
        else:
            self.cols = Cols.Cols(t)

    def stats(self,what,cols,nPlaces):
        def fun(k,col):
            f = getattr(col,what)
            return col.rnd(f(),nPlaces), col.txt
        
        return Misc.kap(cols,fun)
