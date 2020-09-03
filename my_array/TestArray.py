# -*- coding:utf-8 -*-

from sys import *
from time import time
from my_array.DynamicArray import DynamicArray


def dynamic_array(n):
    """
    # 动态数组测量
    """
    data = []
    for k in range(n):
        a = len(data)
        # 查询每个对象在主存中实际占用多少位字节 getsizeof
        b = getsizeof(data)
        print('Length:{0:3d};Size in bytes:{1:4d}'.format(a, b))
        data.append(None)


def compute_average(n):
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end-start) /n


def insertion_sort(A):
    """
    插入排序 O(n)-O(n^2)
    """
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur








if __name__ == "__main__":
    # dynamic_array(24)

    # array = DynamicArray()
    # for k in range(100):
    #     array.append(k)
    # print(array.__len__())
    # print(compute_average(1000000))

    """
    document = "hello 45karma"
    # 列表推导式 创建临时表
    letters1 = ''.join([c for c in document if c.isalpha()])
    print(letters1)
    # 生成器 避免临时表
    letters2 = ''.join(c for c in document if c.isalpha())
    print(letters2)
    """
    A = ['A', 'D', 'C', 'B', 'F', 'E']
    insertion_sort(A)
    print(A)

    pass
