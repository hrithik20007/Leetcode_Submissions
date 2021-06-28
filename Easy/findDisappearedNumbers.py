'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]
'''


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        We can subtract a set from another giving us the numbers/chars left. Also, we know any repeating numbers are deleted from nums when it is converted into 
        a set.
        '''
        return list(set(range(1,len(nums)+1))-set(nums))
        '''
        Time Limit Exceeded
        
        
        j=1
        l=[]
        n=len(nums)
        while(j<=n):
            if j not in nums:
                l.append(j)
            j+=1
            
        return l
        '''
