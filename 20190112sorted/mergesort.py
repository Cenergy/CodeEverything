# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '11/1/2019 11:13 AM'


#递归的写法，自顶向下
def merge_sort(array):
    if len(array)<=1:
        return array
    mid=len(array)//2
    left=array[:mid]
    right=array[mid:]
    left=merge_sort(left)
    right=merge_sort(right)
    return merge(left,right)
def merge(left,right):
    ret=[]
    while left and right:
        if left[0]>right[0]:
            ret.append(right.pop(0))
        else:
            ret.append(left.pop(0))
    if left:
        ret+=left
    if right:
        ret+=right
    return ret
if __name__ == '__main__':
    test = [4, 2, 1, 5, 3]
    print(merge_sort(test))
