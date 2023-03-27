import Misc

class Num:
    def __init__(self, t = []):
        self.n, self.mu = 0, 0
        self.m2, self.sd = 0, 0
        for x in t:
            Misc.add(self, x)