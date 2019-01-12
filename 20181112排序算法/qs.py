# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '12/1/2019 10:35 AM'



def quicksort(lst, l, r):
    if l < r:
        p = partition(lst, l, r)
        quicksort(lst, l, p)
        quicksort(lst, p+1, r)
    return lst

def partition(lst, l, r):
    pivot = lst[r-1]
    i = l - 1
    for j in range(l, r):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    if lst[r-1] < lst[i+1]:
        lst[i+1], lst[r-1] = lst[r-1], lst[i+1]
    return i+1


if __name__ == '__main__':
    test = [4, 2, 1, 5, 3]
    print("Sorted:", quicksort(test,0,len(test)))