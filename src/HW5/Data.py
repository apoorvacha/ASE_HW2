import Misc
from Cols import COLS
# import Cols 
import Rows, Examples
import math, csv, Update
from typing import List, Union


def csv_content(src):
    res = []
    with open(src, mode='r') as file:
        csvFile = csv.reader(file)
        for row in csvFile:
            res.append(row)
    return res



class Data:

    def __init__(self):
        self.cols = None
        self.rows = []


    def read(self, sFile):
        data = Data()
        callback = lambda t: Update.row(data, t)
        Examples.readCSV(sFile, callback)
        return data


    def add(self, t: list[str]):
        if (self.cols):
            
            row = Rows.Rows(t)
            self.rows.append(row.cells)
            self.cols.add(row)
        else:
            print(t)
            self.cols = Cols.COLS(t)

    def stats(self,what,cols,nPlaces):
        def fun(k,col):
            f = getattr(col,what)
            return col.rnd(f(),nPlaces), col.txt
        
        return Misc.kap(cols,fun)

    def clone(self, data, ts=None):
        data1 = Update.row(Data(), data.cols.names)
        for t in ts or []:
            Update.row(data1, t)
        return data1

    def better(self, row1, row2):
        s1, s2, ys = 0, 0, self.cols.y
        for _,col in enumerate(ys):
            x = col.norm(row1[col.at])
            y = col.norm(row2[col.at])
            s1 = s1 - math.exp(col.w * (x - y) / len(ys))
            s2 = s2 - math.exp(col.w * (y - x) / len(ys))
        
        return s1/len(ys) < s2/len(ys)


    def dist(self, row1, row2, cols=None):
        n, d = 0, 0
        for _, col in enumerate(cols or self.cols.x):
            n = n + 1
            val = col.dist(row1[col.at], row2[col.at])
            d = d + val ** 2
        return (d / n) ** (1 / 2)
    
    def around(self, row1, rows = None , cols= None):
        if not rows:
            rows = self.rows
        def fun(row2):
            return {"row": row2, "dist": self.dist(row1, row2, cols)}
        u = map(fun,rows)
        return sorted(u,key = lambda x: x['dist'])




    def cluster(self, rows=None, min_size=None, cols=None, above=None):
        rows = rows or self.rows
        min_val = min_size or (len(rows)) ** 0.5
        if not cols:
            cols = self.cols.x
        node = {"data": self.clone(rows)}
        if len(rows) > 2 * min_val:
            left, right, node["A"], node["B"], node["mid"], temp = self.half(rows, cols, above)
            node["left"] = self.cluster(left, min_val, cols, node["A"])
            node["right"] = self.cluster(right, min_val, cols, node["B"])
        
        return node


    def sway(self, rows=None, min=None, cols=None, above=None):
        rows = rows or self.rows
        min = min or len(rows) ** 0.5
        cols = cols if cols else self.cols.x
        node = {"data": self.clone(rows)}

        if len(rows) > 2 * min:
            left, right, node["A"], node["B"], node["min"], _ = self.half(rows, cols, above)
            if self.better(node["B"], node["A"]):
                left, right, node["A"], node["B"] = right, left, node["B"], node["A"]
            node["left"] = self.sway(left, min, cols, node["A"])

        return node

    def furthest(self, row1, rows, cols, t):
        t = self.around(row1, rows, cols)
        return t[-1]
 

