"""
插入排序，算法思想：
    分组，第一个数字视为有序数组，后续数组视为无序数组
    从无序数组的第一个数，及数组的第二个数开始遍历
    与有序数组中进行比较，放在合适的位置
时间复杂度：O(n^2)
空间复杂度：O(1)
"""


def insert_sort(data_list):
    length = len(data_list)
    for i in range(1, length):
        while i > 0 and data_list[i] < data_list[i - 1]:
            data_list[i], data_list[i - 1] = data_list[i - 1], data_list[i]
            i -= 1
    return data_list


if __name__ == '__main__':
    data = [8, 5, 2, 9, 5, 6, 3]
    print(insert_sort(data))
