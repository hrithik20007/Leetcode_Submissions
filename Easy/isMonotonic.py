'''
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].  An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
Return true if and only if the given array nums is monotonic.

Example 1:
Input: nums = [1,2,2,3]
Output: true

Example 2:
Input: nums = [6,5,4,4]
Output: true

Example 3:
Input: nums = [1,3,2]
Output: false

Example 4:
Input: nums = [1,2,4,5]
Output: true

Example 5:
Input: nums = [1,1,1]
Output: true
'''




class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        c=-1
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                continue
            if c==0 and nums[i+1]<nums[i]:
                return False
            if c==1 and nums[i+1]>nums[i]:
                return False
            if nums[i]<nums[i+1]:
                c=0
            if nums[i]>nums[i+1]:
                c=1
            
        return True
        

#=============================OR===================================== (BOTH WORK)


        if nums==sorted(nums) or nums==sorted(nums)[::-1]:
            return True
        else:
            return False
