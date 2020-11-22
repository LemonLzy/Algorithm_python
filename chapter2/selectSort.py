# @Author:Lzy
# @Time:2020/8/27
# selectSort

"""
1、一种较慢的排序算法
2、选择的大O表示法为O(n^2)
3、选择排序算法思想：
    在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
    从剩余未排序元素中继续寻找最小（大元素），然后放到已排序序列的末尾
    以此类推，直到所有元素均排序完毕
"""


# 选择排序
def selectionSort(array):
    length = len(array)
    for i in range(length):
        smallest_index = i
        for j in range(i + 1, length):
            if array[j] < array[smallest_index]:
                smallest_index = j
        array[i], array[smallest_index] = array[smallest_index], array[i]
    return array


"""
测试，对给定数组进行排序
"""
if __name__ == '__main__':
    my_list = [4, 2, 1, 9, 3, 6, 7]
    print(selectionSort(my_list))

# # 找出数组中的最小元素
# def findSmallest(array):
#     smallest = array[0]
#     smallest_index = 0
#     for i in range(1, len(array)):
#         if array[i] < smallest:
#             smallest = array[i]
#             smallest_index = i
