# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '9/1/2019 9:13 PM'


def selectSort(nums):
    for i in range(len(nums)):
        minIndex=i
        for j in range(i+1,len(nums)):
            if nums[minIndex]>nums[j]:
                minIndex=j
        nums[i],nums[minIndex]=nums[minIndex],nums[i]
    return nums


if __name__ == '__main__':
    abc = [11, 2, 34, 23, 5]
    print(selectSort(abc))
