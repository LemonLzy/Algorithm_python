# @Author:Lzy
# @Time:2020/9/15
# NumElement

"""
编写一个递归函数来计算列表包含的元素数
"""
arr = [1, 2, 3, 'a', 'x', 'yz', (9, 6)]


def count(lst):
    total = 0
    if len(lst) == 0:
        return total
    else:
        # 进入此循环，表示列表不为空，元素数增加1
        total += 1
        # 弹出给定列表的元素
        arr.pop()
        # 返回total数量，并将剩余列表继续调用count函数
        return total + count(lst)


print(count(arr))

"""
参考答案，利用切片移除原列表中的元素，与pop函数同理
"""

# def count(list):
#     if list == []:
#         return 0
#     return 1 + count(list[1:])
