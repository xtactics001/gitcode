# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 08:37:27 2018

@author: yjq13
"""
import time

def timer(func):
#    瞎98搞的计时工具
    def inner(*args,times = 1):
        start = time.time()
        for i in range(times):
            ret = func(*args)
        print(str(func.__name__),f'执行{times}次',time.time() - start)
        return ret
    return inner

def swap(li,x,y):
    li[x],li[y] = li[y],li[x]

# 2.将列表元素反向，O(n)
def reverseList(lyrevs):
    lo = 0
    hi = len(lyrevs) - 1
    while lo < hi :
        swap(lyrevs, lo, hi)
        lo += 1
        hi -= 1

# 3.实现一个pow函数,exp > 0, O(exp)
@timer
def expo(num, exp): 
    temp = num
    if exp == 0:
        result = 1
    else:
        while exp > 1:
            num *= temp
            exp -= 1
        result = num
    return result
        
# 4. 使用题目给出的递归定义实现exop2 ,这里时间复杂是O(logn)
def expo2(num, exp):
    if exp == 0:
        return 1
    elif exp % 2 == 1:
        return num * expo2(num, exp - 1)
    else:
        #这里如果返回expo2(num, exp/2) * expo2(num, exp/2) 则O(n)
        return pow(expo2(num, exp/2), 2)

# 6.修改fib函数，使用记忆技术
def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib2(n, d1 = dict()):
    # 时间
    if n in d1:
        return d1[n]
    elif n < 3:
        d1[n] = 1
        return d1[n]
    else:
        d1[n] = fib2(n-2) + fib2(n - 1)
        return d1[n]

while 1:
	rett = input("   ")
	if rett == 'q':
		break
	else:
		print(len(str(fib2(int(rett)))))
    


    

    

    

