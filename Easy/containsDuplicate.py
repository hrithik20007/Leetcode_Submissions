#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        #If a list has duplicates, then after sorting them, they must be listed one after the other.
        f=0
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                f+=1
        
        if f==0:
            return False
        else:
            return True    
        
