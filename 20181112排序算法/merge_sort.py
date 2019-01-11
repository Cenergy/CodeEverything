# -*- coding:utf-8 -*-


# 合并两个已排好序的区间：[head1, tail1]与[head2, tail2]
def mergeSortHelper(v, head1, head2, tail2):
    tail1 = head2 - 1
    start = head1
    index = 0
    tmp = [0] * (tail2-head1+1)
    while head1 <= tail1 or head2 <= tail2:
        if head1 > tail1:
            tmp[index] = v[head2]
        elif head2 > tail2:
            tmp[index] = v[head1]
        else:
            if v[head1] <= v[head2]:
                tmp[index] = v[head1]
            else:
                tmp[index] = v[head2]

        if head1 <= tail1 and tmp[index] == v[head1]:
            head1 += 1
        else:
            head2 += 1
        index += 1

    for i in range(start, tail2+1):
        v[i] = tmp[i-start]


def mergeSort(v):
    length = len(v)
    step = 1
    # 步长为1,2,4,8，...，一直合并下去
    while step <= length:
        offset = step << 1
        for index in range(0, length, offset):
            mergeSortHelper(v, index, min(index+step, length-1), min(index+offset-1, length-1))
        step = offset
    return v



if __name__ == '__main__':
    test = [4, 2, 1, 5, 3]
    print("original:", test)
    print("Sorted:", mergeSort(test))