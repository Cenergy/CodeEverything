# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '12/11/2018 11:52 AM'


def bubble_sorted(new_list):
    list_len = len(new_list)
    for i in range(list_len - 1):
        for j in range(list_len - 1, i, -1):
            if new_list[j] < new_list[j - 1]:
                new_list[j], new_list[j - 1] = new_list[j - 1], new_list[j]
            # print(new_list)
    return new_list

if __name__ == '__main__':
    abc = [17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 12]
    print(bubble_sorted(abc))