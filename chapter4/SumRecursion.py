# @Author:Lzy
# @Time:2020/9/15
# SumRecursion

"""
给定一个数字数组，使用递归求数组之和。
"""

arr = [2, 4, 6, 8, 10]


def sum(lst):
    total = 0
    # 数组长度为0表示循环完毕，直接返回total
    if len(arr) == 0:
        return total
    else:
        # 每一次循环将数组的最后一位数弹出，与total相加，然后将剩余的数组继续放入sum函数调用
        return total + lst.pop() + sum(lst)


print(sum(arr))

"""
参考答案，利用切片移除原列表中的元素，与pop函数同理
"""

# def sum(list):
#     if list == []:
#         return 0
#     return list[0] + sum(list[1:])
