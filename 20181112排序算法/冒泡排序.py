# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '12/11/2018 11:52 AM'


def bubble_sorted(new_list):
    list_len = len(new_list)
    for i in range(list_len - 1):
        for j in range(list_len - 1, i, -1):
            if new_list[j] < new_list[j - 1]:
                new_list[j], new_list[j - 1] = new_list[j - 1], new_list[j]
    return new_list

if __name__ == '__main__':
    abc = [1, 2, 34, 43, 546, 5, 7, 23, 4, 2, 43, 5, 32, 6, 5, 6, 87, 9, 79, 5, 3, 42]
    print(bubble_sorted(abc))