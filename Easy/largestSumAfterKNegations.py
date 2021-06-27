'''
Given an array nums of integers, we must modify the array in the following way: we choose an i and replace nums[i] with -nums[i], and we repeat this process k times 
in total.  (We may choose the same index i multiple times.)
Return the largest possible sum of the array after modifying it in this way.

Example 1:
Input: nums = [4,2,3], k = 1
Output: 5
Explanation: Choose indices (1,) and nums becomes [4,-2,3].

Example 2:
Input: nums = [3,-1,0,2], k = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].

Example 3:
Input: nums = [2,-3,-1,5,-4], k = 2
Output: 13
Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
'''



#We change the sign of the smallest number during each iteration
class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(k):
            nums.sort()       #Smallest number
            nums[0]*=-1
            
        return sum(nums)
