'''
You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.
    For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.
An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.

Example 1:
Input: nums = [1,1,1]
Output: 3
Explanation: You can do the following operations:
1) Increment nums[2], so nums becomes [1,1,2].
2) Increment nums[1], so nums becomes [1,2,2].
3) Increment nums[2], so nums becomes [1,2,3].

Example 2:
Input: nums = [1,5,2,4,1]
Output: 14

Example 3:
Input: nums = [8]
Output: 0
'''



class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        else:
            f=0

            '''
            Works on the logic such that if a number is smaller than its predecessor then that no. is increased till it is one value more than its predecessor
            and the added value is added to f. f takes each increment value and gives the total necessary operations. In example 2, the increment values are:
            4,3 and 7 (i.e. 14 in total).
            '''
            for i in range(0,len(nums)-1):
                if nums[i]>nums[i+1]:
                    f+=(nums[i]-nums[i+1])+1
                    nums[i+1]+=(nums[i]-nums[i+1])+1
                elif nums[i]==nums[i+1]:
                    f+=1
                    nums[i+1]+=1
                
            return f
