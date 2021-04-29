'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
'''


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        n={}
        
        #We store elements as key and their indices as values in a dictionary. In later iterations, if a match is found as well as satisfies the other condition, then we return True
        for i in range(0,len(nums)):
            if nums[i] in n and abs(i-n[nums[i]])<=k:
                return True
            else:
                n[nums[i]]=i
                
        return False
        '''
        c=0
        i=0
        j=len(nums)-1
        while(i<j):
            if nums[i]==nums[j] and abs(i-j)<=k:
                c+=1
            i+=1
            j-=1
                
        if c==0:
            return False
        else:
            return True
        '''
        '''
        Time limit exceeded
        
        c=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and abs(i-j)<=k:
                    c+=1
        
        if c==0:
            return False
        else:
            return True
        '''
