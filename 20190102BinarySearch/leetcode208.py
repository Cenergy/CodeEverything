# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '2/1/2019 10:22 PM'



# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j]:
                if i==j:
                    pass
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                i=i+1
        return nums

if __name__ == '__main__':
    a=Solution()
    print(a.moveZeroes(list([0,1,0,3,12])))