#!/usr/env python
import sys
sys.path.append("../lib/ThinkBayes2/code/")
from thinkbayes2 import Pmf

class Monty(Pmf):
    def __init__(self, hypos):
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()

hypos = 'ABC'
pmf = Monty(hypos)
print(pmf)

print("Finished")
