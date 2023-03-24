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
  