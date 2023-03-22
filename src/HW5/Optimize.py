# -- ## Optimization

# -- Recursively prune the worst half the data. Return
# -- the survivors and some sample of the rest.
# function sway(data,     worker,best,rest)
#   function worker(rows,worse,  above)
#     if   #rows <= (#data.rows)^the.min 
#     then return rows, many(worse, the.rest*#rows) 
#     else local l,r,A,B = half(data, rows, cols, above)
#          if better(data,B,A) then l,r,A,B = r,l,B,A end
#          map(r, function(row) push(worse,row) end) 
#          return worker(l,worse,A) end 
#   end ----------------------------------
#   best,rest = worker(data.rows,{})
#   return DATA.clone(data,best), DATA.clone(data,rest) end 

import List, Query
from Start import the
from Cluster import half



def sway(data):
      def worker(rows, worse, above = None):
        if len(rows) <= len(data.rows)**(0.5):
            print('Inside if')
            return rows, List.many(worse, the["rest"] * len(rows))
        else:
            l , r, A, B,_ = half(data, rows, None, above)
            if Query.better(data, B, A):
                l, r, A, B = r, l, B, A
            for row in r:
                worse.append(row)
            return worker(l, worse, A)

      best, rest = worker(data.rows, [])
      return data.clone(data, best), data.clone(data, rest)
    # def worker(rows, worse, above=None):
    #     if len(rows) <= len(data.rows)**(0.5):
    #         print('Inside if')
    #         return rows, List.many(worse, the["rest"] * len(rows))
    #     else:
    #         print('Inside else')
    #         l, r, A, B, _ = half(data, data.rows , None, above)
    #         if Query.better(data, B, A):
    #             l, r, A, B = r, l, B, A
    #         for row in r:
    #             worse.append(row)
    #         return worker(l, worse, A)

    # best, rest = worker(data.rows, [])
    # return data.clone(data, best), data.clone(data, rest)
# def worker(rows, worse, above = None):
#         if len(rows) <= len(data.rows) ** util.args.min:
#             return rows, many(worse, util.args.rest*len(rows))
#         else:
#             l , r, A, B,_ = half(data, rows, None, above)
#             if query.better(data, B, A):
#                 l, r, A, B = r, l, B, A
#             for row in r:
#                 worse.append(row)
#             return worker(l, worse, A)
#     best, rest = worker(data.rows, [])
#     return data.clone(data, best), data.clone(data, rest)