# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '8/11/2018 2:12 PM'


def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = [1] + nums + [1]
    l = len(nums)
    dp = [[0] * l for _ in range(l)]
    for i in range(2, l):
        for j in range(l - i):
            r = i + j
            t = nums[j] * nums[r]
            dp[j][r] = max(t * nums[k] + dp[j][k] + dp[k][r] for k in range(j + 1, r))

    print(dp)
    return dp[0][l - 1]



print(maxCoins([3,1,5,8]))