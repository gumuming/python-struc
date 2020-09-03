# -*- coding:utf-8 -*-
import math


def binary_search(data, target, low, high):
    """
    二分查找 适用于有序数组 递归实现
    """
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


def binary_search_iterative(data, target):
    """
    二分查找算法的非递归实现
    :param data:
    :param target:
    :return: True
    """
    low = 0
    high = len(data) -1
    while low < high:
        mid = abs(high-low) // 2 + low
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid -1
        else:
            low = mid +1
    return False





def linear_sum(S, n):
    """
    递归计算数字和
    """
    if n == 0:
        return 0
    else:
        return linear_sum(S, n - 1) + S[n - 1]


def reverse(S, start, stop):
    """
    线性递归逆置序列元素
    :param S:
    :param start:
    :param stop:
    :return:
    """
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)


def reverse_iterative(S):
    """
    迭代逆置一个序列的元素
    :param S:
    :return:
    """
    start, stop = 0, len(S)
    while start < stop - 1:
        # swap first and last
        S[start], S[stop-1] = S[stop -1], S[start]
        # narrow the range
        start, stop = start+1, stop -1


def power(x, n):
    """
    计算幂的递归算法 x^n = x * x^(n-1)
    时间复杂度 O(n)
    :param x: 
    :param n: 
    :return: 
    """
    if n == 0:
        return 1
    else:
        return x*power(x, n-1)


def power(x, n):
    """
    计算幂的递归算法 改进  x^n = x * power(x,|n/2|)^2
    时间复杂度 O(logn)
    :param x:
    :param n:
    :return:
    """
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result


def binary_sum(S, start, stop):
    """
    二路递归调用 计算序列元素之和
    二路递归: 一个函数执行两个递归调用
    时间复杂度 O(logn)
    :param S:
    :param start:
    :param stop:
    :return:
    """
    if start > stop:
        return 0
    elif start == stop-1:
        return S[start]
    else:
        mid = abs(stop-start) // 2 + start
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = binary_search(data=array, target=3, low=0, high=7)
    print(res)
