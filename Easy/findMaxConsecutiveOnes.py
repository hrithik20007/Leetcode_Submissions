'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
'''



class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f=0
        c=-1
        c1=0
        for i in nums:
            if i==1:
                f+=1
                c1=f
            if i==0:
                c1=f
                f=0
            if c<c1:
                c=c1
                
        return c
