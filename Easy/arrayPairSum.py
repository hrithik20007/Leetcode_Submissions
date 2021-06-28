'''
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

Example 1:
Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.
'''




class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        Logic is that if you want to get a big no. from a min function, it should be paired with a bigger no. Thus for sum to be maximum, we have to try
        and pair the bigger nos. together like (1,2) and (5,6) -- not (1,5) and (2,6). In first case, sum is 6 while for second, it is 3.
         '''
        s=sum(sorted(nums)[::2])    #sorted() has a return type unlike sort()
        return s

        '''
        This is my solution but I wanted a faster solution 
        
        
        nums.sort()
        s=0
        for i in range(0,len(nums),2):
            r=min(nums[i],nums[i+1])
            s+=r
            
        return s
        '''
