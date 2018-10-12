# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 15:10:51 2018

@author: yjq13
"""

import time
from collections import Counter


problemSize = 100000
print("%12s%16s" % ("Problem Size", "Seconds"))
for count in range(5):
    start = time.time()
    work = 1
    for x in range(problemSize):
        work += 1
        work -= 1
    elapsed = time.time()-start
    print("%12d%16.3f" % (problemSize,elapsed))
    problemSize *= 2

