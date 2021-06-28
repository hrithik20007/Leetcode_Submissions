'''
Given an array nums of integers, for each integer nums[i] we may choose any x with -k <= x <= k, and add x to nums[i].
After this process, we have some array result.
Return the smallest possible difference between the maximum value of result and the minimum value of result.

Example 1:
Input: nums = [1], k = 0
Output: 0
Explanation: result = [1]

Example 2:
Input: nums = [0,10], k = 2
Output: 6
Explanation: result = [2,8]

Example 3:
Input: nums = [1,3,6], k = 3
Output: 0
Explanation: result = [3,3,3] or result = [4,4,4]
'''





class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if len(nums)==1:                #As there is no bigger or smaller number to compare, difference is always 0
            return 0
        nums.sort()
        n1=nums[0]                      #Smallest number
        n2=nums[-1]                     #Largest number
        n1+=k
        n2-=k
        if n1<n2:
            return n2-n1
        else:
            return 0
