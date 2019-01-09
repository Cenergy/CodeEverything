# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '9/1/2019 9:13 PM'


def selection_sort(arr):
    for i in range(len(arr)):
        minIndex=i
        for j in range(i+1,len(arr)):
            if arr[minIndex]>arr[j]:
                minIndex=j
        if i==minIndex:
            pass
        else:
            arr[i],arr[minIndex]=arr[minIndex],arr[i]
    return arr


if __name__ == '__main__':
    testlist = [17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 12]
    print(selection_sort(testlist))
