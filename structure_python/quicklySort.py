# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 06:27:09 2018

@author: yjq13
"""
import random
import math


def quicklySort(lyst):
    quickSortHelper(lyst, 0, len(lyst)-1)


def quickSortHelper(lyst, left, right):
    global counst 
    if left < right:
        pivotLocation = partition(lyst, left, right)
        quickSortHelper(lyst, left, pivotLocation - 1)
        quickSortHelper(lyst,pivotLocation+1, right)
        
def partition(lyst, left, right):
    global counst
    
    # 找出基准点（pivot），并将其和最后子列最后一个元素互换
    middle = (left + right)//2
    pivot = lyst[middle]
    lyst[middle],lyst[right] = lyst[right], pivot    
    #在自列表一个位置设置边界点
    boundary = left
    #扫描整个子列，将比基准点小的元素移动至子列头
    for index in range(left, right):
        counst +=1
        if lyst[index] < pivot:
            lyst[index], lyst[boundary] = lyst[boundary],lyst[index]
            boundary += 1
    #将基准点元素放置在边界点的位置，既排序正确的位置
    lyst[right], lyst[boundary] = lyst[boundary], lyst[right]
    return boundary
counst = 0
lyst = []
print(f"{'size':<20} {'counst':<20} {'counst-len(lyst)':<20}")
li = [pow(2,x) for x in range(1,18)]
for size in li:
    for count in range(size):
        lyst.append(random.randint(1,size+1))
    quicklySort(lyst)
    print(f'{size:<20} {counst:<20} {math.log2(size):<20}')

    