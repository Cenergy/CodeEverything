# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '11/1/2019 11:46 PM'




def quick_sort(array,l,r):
    if l<r:
        p=partition(array,l,r)
        quick_sort(array,l,p-1)
        quick_sort(array,p,r)
    return array

def partition(array,l,r):
    v=array[l]
    j=l
    for i in range(l+1,r):
        if array[i]<v:
            temp=array[i]
            array[i]=array[j+1]
            array[j + 1]=temp

            # array[j+1],array[i]=array[i],array[j+1]
        j=j+1
        print(array)
    array[l],array[j]=array[l],array[j]
    return j


if __name__ == '__main__':
    test = [2,0, 6,1, 4, 5, 3]
    n=len(test)
    print(partition(test,0,len(test)))
