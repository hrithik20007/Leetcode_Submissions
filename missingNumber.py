'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
'''



class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        This solution also works but I've gone with the lower solution because it is asked for O(1) space complexity and O(n) runtime complexity.

        
        n=len(nums)
        nums.sort()
        if nums[n-1]==n-1:
            return n
        elif nums[0]!=0:
            return 0
        else:
            k=0
            for i in range(0,n):
                if nums[i]!=k:
                    s=k
                    break
                k+=1
            return s
        '''
        return sum([i for i in range(len(nums)+1)])-sum(nums)
