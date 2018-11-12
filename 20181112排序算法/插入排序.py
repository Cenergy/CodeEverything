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

if __name__ == '__main__':
    abc = [1, 2, 34, 43, 546, 5, 7, 23, 4, 2, 43, 5, 32, 6, 5, 6, 87, 9, 79, 5, 3, 42]
    print(insert_sort(abc))