'''
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3,4]
Output: 24
'''


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-3]*nums[-2]*nums[-1],nums[0]*nums[1]*nums[-1])     #The first two numbers may be negative and their products may be larger  Eg:[-78,-36,-5,1,2,3].
