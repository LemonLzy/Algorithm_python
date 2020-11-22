"""
冒泡排序，算法思想：
    比较相邻的元素，如果第一个比第二个大，就交换位置
    第一次从第一位开始比较，第二次从第二位开始比较，以此类推
"""


def bubble(data_list):
    length = len(data_list)
    for i in range(0, length):
        # 标记位，如果一次循环中标记为仍然为0，这说明已排好序，无需继续循环
        flag = 0
        for j in range(i + 1, length):
            if data_list[i] > data_list[j]:
                data_list[i], data_list[j] = data_list[j], data_list[i],
                flag = 1
        if flag == 0:
            break
    return data_list


if __name__ == '__main__':
    data = [1, 33, 44, 46, 36, 22]
    print(bubble(data))
