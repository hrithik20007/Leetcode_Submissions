'''
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Example 2:
Input: nums = [1,2,3,4]
Output: 2

Example 3:
Input: nums = [1,1,1,1]
Output: 0
'''





class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        r=0

        '''
        Making a dictionary to get the frequencies of all characters. get() is used to return the value of the key specified. If the key does not exist, then it 
        returns the value specified in the second parameter.
        '''
        for i in nums:
            d[i]=d.get(i,0)+1

        for i in nums:      
            if i+1 in d:    #This condition is checked for every value of nums. So, with 3, it will check for 4 and for 2, it will check for 3; keeping the difference as 1 always. 
                r=max(d[i]+d[i+1],r)

        return r
        '''
        l=[]
        r=[]
        l.append(nums[0])
        for i in range(1,len(nums)):
            for j in range(i,len(nums)):
                n=min(l)
                if l[0]==nums[j] or abs(n-nums[j])==1 or abs(n-nums[j])==0:
                    l.append(nums[j])
            
            if len(list(set(l)))==1:
                l=[]
            if len(r)<len(l):
                r=l[:]
                
            l=[]
            l.append(nums[i])

        return len(r)
        '''
