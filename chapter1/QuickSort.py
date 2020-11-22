"""
快速排序，算法思想：
    选取基准值
    比基准值小的分成一个数组，比基准值大的分成另一个数组
    对剩余两个数组进行递归，再次选取基准值排序
    直到数组长度小于2即可返回
"""


def quick_sort(data_list):
    # 基线条件：为空或只包含一个元素，这样的数组是有序的
    if len(data_list) < 2:
        return data_list

    standard = data_list[0]
    less = [i for i in data_list[1::] if i <= standard]
    more = [i for i in data_list[1::] if i > standard]
    return quick_sort(less) + [standard] + quick_sort(more)


if __name__ == '__main__':
    data = [19, 5, 3, 2, 3, 1, 6, 30]
    print(quick_sort(data))
