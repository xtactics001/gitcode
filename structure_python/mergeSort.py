# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 06:27:30 2018

@author: yjq13
"""
import numpy as np
import random

def mergeSort(lyst):
    """生成一个缓存数组，传入mSH函数"""    
    copyBuffer = np.array([0 for x in range(len(lyst))])
    mergeSortHelper(lyst, copyBuffer, 0, len(lyst)-1)
    
def mergeSortHelper(lyst, copyBuffer, low, high):
    """分割列表，"""
    if low < high: 
        middle = (low + high) // 2
        mergeSortHelper(lyst, copyBuffer, low, middle)
        mergeSortHelper(lyst, copyBuffer, middle + 1, high)
        merge(lyst, copyBuffer, low, middle, high)
    
def merge(lyst, copyBuffer, low, middle, high):
    '''合并分割后的子序列'''
    i1 = low     #定义指向第一个表头的指针 
    i2 = middle + 1 #定义指向后一个表头的指针
    
    for i in range(low, high + 1):
        """当一个表元素全部被合并后，将另一个表剩余元素依次加入copyBuffer"""
        if i1 > middle:   
            copyBuffer[i] = lyst[i2]
            i2 += 1
        elif i2 > high:
            copyBuffer[i] = lyst[i1]
            i1 += 1
            """依次比较需合并两个表的表头元素，将小的元素加入copyBuffer"""
        elif lyst[i1] < lyst[i2]:
            copyBuffer[i] = lyst[i1]
            i1 += 1
        else:
            copyBuffer[i] = lyst[i2]
            i2 += 1
    
    for i in range(low, high + 1):
        lyst[i] = copyBuffer[i]

def test():
    size = 10
    lyst = list(range(10))
    random.shuffle(lyst)
    print(lyst)
    mergeSort(lyst)
    print(lyst)

test()

#lyst = []
#print(f"{'size':<20} {'counst':<20} {'counst-len(lyst)':<20}")
#li = [pow(2,x) for x in range(1,5)]
#for size in li:
#    for count in range(size):
#        lyst.append(random.randint(1,size+1))
#    mergeSort(lyst)
#    print(f'{size:<20} {counst:<20} {math.log2(size):<20}')
#    print(lyst)


    




