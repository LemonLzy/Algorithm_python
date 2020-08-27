# @Author:Lzy
# @Time:2020/8/27
# selectSort

"""
1、一种较慢的排序算法
2、选择的大O表示法为O(n^2)
"""


# 找出数组中的最小元素
def findSmallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


# 选择排序
def selectionSort(array):
    new_array = []
    for i in range(len(array)):
        smallest = findSmallest(array)
        # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值，即从原数组中移除最小的值，并将最小的值返回，加入到新数组
        new_array.append(array.pop(smallest))
    return new_array


"""
测试，对给定数组进行排序
"""
my_list = [1, 2, 3, 4, 5, 6, 7]
print(selectionSort(my_list))
