# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '1/11/2018 5:31 PM'



# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    sign = lambda x: x and (1, -1)[x < 0]
    print(sign)
    r = int(str(sign(x) * x)[::-1])
    print(r)
    # return (sign(x) * r, 0)[r > 2 ** 31 - 1]
    return (sign(x) * r, 0)[r > 2 ** 31 - 1]


print(reverse(-123))