# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '3/1/2019 11:37 PM'


# 最小连续长度的子数组总和
# 给定的阵列Ñ正整数，且为正整数小号，找到的最小长度的连续子数组，其sum ≥ s。如果没有，则返回0。
#
# 例：
# 输入： s = 7, nums = [2,3,1,2,4,3]
# 输出： 2

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = -1  # [l,r]是我们的滑动窗口
        sum = 0
        res = len(nums) + 1
        while l < len(nums):
            if sum < s and r + 1 < len(nums):
                r = r + 1
                sum = sum + nums[r]
            else:

                sum = sum - nums[l]
                l = l + 1

            if sum >= s:
                res = min(res, r - l + 1)
        if res == len(nums) + 1:
            res = 0
        return res
