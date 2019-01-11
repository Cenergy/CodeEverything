# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '12/11/2018 11:44 AM'


def insert_sort(lst):
    n=len(lst)
    if n==1:
        return lst
    for i in range(1,n):
        for j in range(i,0,-1):
            if lst[j]<lst[j-1]:
                lst[j],lst[j-1]=lst[j-1],lst[j]
            else:
                break
    return lst

def insert_sort2(lst):
    n=len(lst)
    if n==1:
        return lst
    for i in range(1,n):
        item_arr=lst[i]
        j=i
        for j in range(i,0,-1):
            if lst[j-1]>item_arr:
                lst[j] = lst[j-1]
            else:
                break
            lst[j-1]=item_arr
    return lst
def insertion_sort(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and temp < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp
    return lst
# 对区间[l,r]进行排序
def insert_sort3(lst,l,r):
    n=len(lst)
    if n==1:
        return lst
    for i in range(l+1,r+1):
        item_arr=lst[i]
        j=i
        for j in range(i,l,-1):
            if lst[j-1]>item_arr:
                lst[j] = lst[j-1]
            lst[j-1]=item_arr
    return lst





if __name__ == '__main__':
    abc = [11, 4, 3, 2, 546, 5, 7, 23, 4, 2, 43, 5, 32, 6, 5, 6, 87, 9, 79, 5, 3, 42]
    print(insert_sort3(abc,1,5))