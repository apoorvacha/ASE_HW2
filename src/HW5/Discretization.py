# -- ## Discretization

# -- Return RANGEs that distinguish sets of rows (stored in `rowss`).
# -- To reduce the search space,
# -- values in `col` are mapped to small number of `bin`s.
# -- For NUMs, that number is `the.bins=16` (say) (and after dividing
# -- the column into, say, 16 bins, then we call `mergeAny` to see
# -- how many of them can be combined with their neighboring bin).
# function bins(cols,rowss)
#   local out = {}
#   for _,col in pairs(cols) do
#     local ranges = {}
#     for y,rows in pairs(rowss) do
#       for _,row in pairs(rows) do
#         local x,k = row[col.at]
#         if x ~= "?" then
#           k = bin(col,x)
#           ranges[k] = ranges[k] or RANGE(col.at,col.txt,x)
#           extend(ranges[k], x, y) end end end
#     ranges = sort(map(ranges,itself),lt"lo")
#     out[1+#out] = col.isSym and ranges or mergeAny(ranges) end
#   return out end

# -- Map `x` into a small number of bins. `SYM`s just get mapped
# -- to themselves but `NUM`s get mapped to one of `the.bins` values.
# -- Called by function `bins`.
# function bin(col,x,      tmp)
#   if x=="?" or col.isSym then return x end
#   tmp = (col.hi - col.lo)/(the.bins - 1)
#   return col.hi == col.lo and 1 or m.floor(x/tmp + .5)*tmp end

# -- Given a sorted list of ranges, try fusing adjacent items
# -- (stopping when no more fuse-ings can be found). When done,
# -- make the ranges run from minus to plus infinity
# -- (with no gaps in between).
# -- Called by function `bins`.
# function mergeAny(ranges0,     noGaps)
#   function noGaps(t)
#     for j = 2,#t do t[j].lo = t[j-1].hi end
#     t[1].lo  = -m.huge
#     t[#t].hi =  m.huge
#     return t 
#   end ------
#   local ranges1,j,left,right,y = {},1
#   while j <= #ranges0 do
#     left, right = ranges0[j], ranges0[j+1]
#     if right then
#       y = merge2(left.y, right.y)
#       if y then
#         j = j+1 -- next round, skip over right.
#         left.hi, left.y = right.hi, y end end
#     push(ranges1,left)
#     j = j+1 
#   end
#   return #ranges0==#ranges1 and noGaps(ranges0) or mergeAny(ranges1) end

# -- If the whole is as good (or simpler) than the parts,
# -- then return the 
# -- combination of 2 `col`s.
# -- Called by function `mergeMany`.
# function merge2(col1,col2,   new)
#   new = merge(col1,col2)
#   if div(new) <= (div(col1)*col1.n + div(col2)*col2.n)/new.n then
#     return new end end

# -- Merge two `cols`. Called by function `merge2`.
# function merge(col1,col2,    new)
#   new = copy(col1)
#   if   col1.isSym 
#   then for x,n in pairs(col2.has) do add(new,x,n) end
#   else for _,n in pairs(col2.has) do add(new,n)   end
#        new.lo = m.min(col1.lo, col2.lo)
#        new.hi = m.max(col1.hi, col2.hi) end 
#   return new end

from Col import COL
from Range import *
from Data import *
import Update as update
from Query import *
import math
from copy import deepcopy

def bins(cols, rowss):
    """
    Function: 
        bins
    Description:
        Computes the bins (ranges of values) for a list of 
        columns based on the values of each column in a list of rows.
    Input:
        cols
            a list of columns to compute the bins for.
        rowss: 
            a dictionary of rows where each key represents a row label and the value is a list of values for each column.
    Output:
        out
            a list of computed bins (ranges of values) for each column. 
            Each bin is represented as a list of Range objects. If the column is symbolic, 
            the list will only contain Range objects. If the column is not symbolic, 
            the list may contain merged ranges of adjacent bins.
    """
    out = []
    for col in cols:
        ranges = {}
        for y, rows in rowss.items():
            for row in rows:
                if (isinstance(col, COL)):
                    col = col.col
                x = row[col.at]
                if x != "?":
                    k = int(bin(col, float(x) if x != "?" else x))
                    ranges[k] = ranges[k] if k in ranges else RANGE(col.at, col.txt, float(x) if x != "?" else x)
                    update.extend(ranges[k], float(x), y)
        ranges = {key: value for key, value in sorted(ranges.items(), key=lambda x: x[1].lo)}
        newRanges = {}
        i = 0
        for key in ranges:
            newRanges[i] = ranges[key]
            i += 1
        newRangesList = []
        if hasattr(col, "isSym") and col.isSym:
            for item in newRanges.values():
                newRangesList.append(item)
        out.append(newRangesList if hasattr(col, "isSym") and col.isSym else mergeAny(newRanges))
    return out

def bin(col, x):
    """
    Function:
        bin
    Description:
        The bin function takes a column object col and a value x as 
        input and returns the corresponding bin value for x based on 
        the range of col. If x is "?" or col is a symbol column, then 
        the function simply returns x.
    Input:
        col - A column object containing the range of values to be binned.
        x - A value to be binned.
    Output:
        The corresponding bin value for x based on the range of col.
    """
    if x=="?" or hasattr(col, "isSym"):
        return x
    tmp = (col.hi - col.lo)/(16 - 1)
    return 1 if col.hi == col.lo else math.floor(x / tmp + 0.5) * tmp

def mergeAny(ranges0):
    """
    Function:
        mergeAny
    Description:
        The mergeAny function takes a list of range objects ranges0 
        as input and recursively merges adjacent ranges until there 
        are no more adjacent ranges to merge. The resulting ranges 
        are returned in a list.
    Input:
        ranges0 - A list of range objects.
    Output:
        A list of range objects resulting from merging adjacent ranges in ranges0.
    """
    def noGaps(t):
        for j in range(1, len(t)):
            t[j].lo = t[j-1].hi
        t[0].lo = -float("inf")
        t[-1].hi = float("inf")
        return t
    ranges1, j = [], 0
    while j < len(ranges0):
        left, right = ranges0[j], ranges0[j+1] if j + 1 < len(ranges0) else None
        if right:
            y = merge2(left.y, right.y)
            if y:
               j = j+1
               left.hi, left.y = right.hi, y
        ranges1.append(left)
        j += 1
    return noGaps(ranges0) if len(ranges1)==len(ranges0) else mergeAny(ranges1)

def merge2(col1, col2):
    """
    Function:
        merge2
    Description:
        The merge2 function takes two columns col1 and col2 as inputs,
        merges them using the merge function, and returns the merged 
        column if the distance between the merged column and the individual
        columns is less than or equal to the expected distance based on their sizes.
    Input:
    col1 - A column object containing data to be merged.
    col2 - A column object containing data to be merged with col1.
    Output:
        The merged column if the distance between the merged column
        and the individual columns is less than or equal to the expected
        distance based on their sizes. Otherwise, no output is returned.
    """
    new = merge(col1, col2)
    if div(new) <= (div(col1)*col1.n + div(col2)*col2.n)/new.n:
        return new

def merge(col1, col2):
    """
    Function:
        merge
    Description:
        The merge function takes two columns col1 and col2 as inputs and returns
        a new column that contains all the data from both input columns. If col1
        has the isSym attribute set to True, it merges the data in col2 with the
        data in col1 using the has dictionary. Otherwise, it merges the data using
        the has list. Additionally, if col1 does not have the isSym attribute set to True, 
        it updates the lo and hi attributes of the new column to the minimum and maximum 
        values of the lo and hi attributes of the input columns, respectively.
    Input:
        col1 - A column object containing data to be merged.
        col2 - A column object containing data to be merged with col1.
    Output:
        A new column object that contains all the data from col1 and col2.
    """
    new = deepcopy(col1)
    if hasattr(col1, "isSym") and col1.isSym:
        for x, n in col2.has.items():
            update.add(new, x, n)
    else:
        for n in col2.has:
            update.add(new, n)
        new.lo = min(col1.lo, col2.lo)
        new.hi = max(col1.hi, col2.hi)
    return new