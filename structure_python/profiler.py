# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 09:16:28 2018
定义Profiler类
用于简单测试排序算法性能
p = Profiler()
p.test(sortFunction, size= , comp= ,exch= , trace= )
@author: yjq13
"""

import time
import random

class Profiler:
    
    def test(self, function, lyst = None, size = 10, unique = True, 
             comp = True, exch = True, trace = False):
        """
        function：需要测试的排序算法
        lyst: 允许使用自定义测试列表
        size：自动生成列表大小
        unique： 列表元素是否重复
        comp：是否打印比较次数
        exch：是否打印交换次数
        trace：是否打印每次交换后的列表
        """
        self._comp = comp
        self._exch = exch
        self._trace = trace
        if lyst != None:
            self._lyst = lyst
        elif unique:
             #此处原书为 self._lyst = range(1,size +1),可能有问题
            self._lyst = list(range(1,size + 1)) 
            random.shuffle(self._lyst)
        else:
            self._lyst = []
            for count in range(size):
                self._lyst.append(random.randint(1,size+1))
        self._exchCount = 0
        self._compCount = 0
        self._startClock()
        function(self._lyst, self)
        self._stopClock()
        print(self)
        
        
    def exchange(self):
        if self._exch:
            self._exchCount += 1
        if self._trace:
            print(self._lyst)
    
    def comparison(self):
        if self._comp:
            self._compCount += 1
    
    def _startClock(self):
        self._start = time.time()
    
    def _stopClock(self):
        self._elapsedTime = round(time.time() - self._start, 3)
        
    def __str__(self):
        resule = "Problem size: "
        resule += str(len(self._lyst)) + "\n"
        resule += "Elapsed time: "
        resule += str(self._elapsedTime) + "\n"
        if self._comp:
            resule += "Comparisons: "
            resule += str(self._compCount) + "\n"
        if self._exch:
            resule += "Exchanges: "
            resule += str(self._exchCount) + "\n"
        return resule
            
    
