# @Author:Lzy
# @Time:2020/8/27
# dichotomy

"""
1、仅当列表是有序时，二分查找才有用。
2、二分查找的大O表示法为O(logn)，对数时间
3、大O表示法讨论的不是时间，而是随着输入的增加，其运行时间将以什么样的速度增加
"""
import math


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low < high:
        # 如果mid不是整数，则向下取整
        mid = math.floor((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
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
