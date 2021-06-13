# @Author:Lzy
# @Time:2020/8/27
# dichotomy

"""
1、仅当列表是有序时，二分查找才有用。
2、二分查找的大O表示法为O(logn)，对数时间：当算法过程出现循环折半的时候，时间复杂度一定会出现logn
3、大O表示法讨论的不是时间，而是随着输入的增加，其运行时间将以什么样的速度增加

常见的时间复杂度排序：
O(1)<O(logn)<O(n)<O(nlogn)<O(n^2)<O(n^2logn)<O(n^3)
"""
import math


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low < high:
        # 如果mid不是整数，则向下取整
        mid = math.floor((low + high) / 2)
        # 根据索引获取列表中中间位置的值guess
        guess = list[mid]
        if guess == item:
            return mid
        # 通过将中间位置的列表值与给定数据进行对比，缩小范围
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1

    return None


"""
测试，查找列表my_list中元素2的索引
"""
my_list = [1, 2, 3, 4, 5, 6, 7]
print(binary_search(my_list, 2))
