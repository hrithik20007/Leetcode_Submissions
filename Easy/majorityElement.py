'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #An element which appears more than n/2 times should be present at the middle when the list is sorted.(n being the list size)
        nums.sort()
        n=len(nums)/2
        return nums[n]
        '''
        Time limit exceeded
        
        
        max_freq=-1
        for i in nums:
            max_freq=max(nums.count(i),max_freq)
        
        for i in nums:
            if nums.count(i)==max_freq:
                return i
        '''
        '''
        p=[0]
        max_freq=-1
        nums.sort()
        for i in range(1,len(nums)):
            if (nums[i]!=nums[i-1]):
                p.append(i)
        p.append(len(nums))
        
        for j in range(1,len(p)):
            freq=p[j]-p[j-1]
            max_freq=max(max_freq,freq)
            
        for k in range(1,len(p)):
            if p[k]-p[k-1]==max_freq:
                s=k
            
        return nums[s-1]
        '''
