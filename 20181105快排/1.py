# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '5/11/2018 10:38 PM'

#快排的时间复杂度nlogn


def quicksort(array):
    if(len(array))<2:
        return array
    else:
        pivot=array[0]
        less=[x for x in array[1:] if x<=pivot]
        greater=[i for i in array[1:] if i>pivot]
        return quicksort(less)+[pivot]+quicksort(greater)



print(quicksort([10,7,9,6,8,3,7,5,1,2,3,4,5,1,21,41,12,12,412,41,192,24,12]))