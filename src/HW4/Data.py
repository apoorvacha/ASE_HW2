from Misc import *
from Cols import *
from Row import *
import math, csv
from typing import List

def csv_content(src):
    res = []
    with open(src, mode='r') as file:
        csvFile = list(csv.reader(file))
        res.append(csvFile)

    return res

class Data:
    def __init__(self,src):
        self.rows = []
        self.cols = None

        if type(src) == str:
            csv_list = csv_content(src)
            for content in csv_list:
                for row in content:
                    row_cont = []
                    for val in row:
                        row_cont.append(val.strip())
                    self.add(row_cont)

        elif type(src) == List[str]:
            self.add(src)


    def add(self,t:list[str]):

        if (self.cols):
            row = Row(t)
            self.rows.append(row)
            self.cols.add(row)
        else:
            self.cols = Cols(t)


    def clone(self,init= []):
        data = Data({self.Cols.names})
        return data


    def stats(self, what, cols: Cols, n_places):
        def fun(k, col):
            return col.rnd(getmetatable(col, what), n_places), col.txt
        # return Misc.kap(cols, fun)
        return kap(cols, fun)


    def dist(self, row1, row2, cols, n, d):
        n, d = 0, 0
        for _, col in enumerate(cols or self.cols.x):
            n = n + 1
            d = d + col.dist(row1[col.at], row2[col.at]) ** 2
        return (d / n) ** (1 / 2)


    def around(self, row1, rows, cols): # Doubt
        new_rows = [(row2, self.dist(row1, row2, cols)) for row2 in (rows or self.rows)]
        return sorted(new_rows, key = lambda x : x[1])

    def furthest(self, row1, rows, cols, t):
        t = self.around(row1, rows, cols)
        return t[-1]

    def half(self, rows, cols, above): # Doubt, incomplete
        def project(row, x, y):
            x, y = cosine(dist(row, A), dist(row, B), c)
            row['x'], row['y'] = row.get('x', x), row.get('y', y)
            return {'row':row, 'x':x, 'y':y}
        def dist(row1, row2):
            return self.dist(row1, row2, cols)
        rows = rows or self.rows
        #A = above or any(rows)
        B = self.furthest(A,rows)['row']
        c = dist(A,B)
        left, right = [], []
        for n, tmp in 

    def cluster(self, rows=None, min_size=None, cols=None, above=None):
        rows = rows or self.rows
        min_val = min_val or (len(rows)) ** 0.5
        if not cols:
            cols = self.cols.x
        node = {"data": self.clone(rows)}
        if len(rows) > 2 * min_val:
            left, right, node["A"], node["B"], node["mid"], temp = self.half(rows, cols, above)
            node["left"] = self.cluster(left, min_val, cols, node["A"])
            node["right"] = self.cluster(right, min_val, cols, node["B"])
        
        return node

