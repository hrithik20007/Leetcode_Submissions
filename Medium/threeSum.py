'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
'''




class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        if len(nums)==3:
            if sum(nums)==0:
                return [nums]
            else:
                return []
        nums.sort()
        l1=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:  #To skip the same elements
                continue
            m=i+1           #m is one more than our value under consideration.. so it is actually the middle pointer, while our element is the left pointer
            r=len(nums)-1   #r is the right pointer
            while(m<r):
                k=nums[i]+nums[m]+nums[r]
                if k>0:
                    r-=1
                elif k<0:
                    m+=1
                else:
                    l1.append([nums[i],nums[m],nums[r]])
                    m+=1    #Since we have to change atleast one value before the loop repeats otherwise which it will become an infinite loop 
                    while(m<r and nums[m]==nums[m-1]):  #To increase l until l has a new value
                        m+=1
        return l1



        '''
        if len(nums)<3:
            return []
        if len(nums)==3:
            if len(list(set(nums)))==3:
                return [nums]
            else:
                return []
        
        nums.sort()
        if 0 in nums:
            i=nums.index(0)
            l=i-1
            r=i+1
        else:
            for i in range(nums):
                if nums[i]>0:
                    r=i
                    l=i-1
                    break
        if l<0 or r>=len(nums):
            return []
        j=-1
        l2=[]
        while(j<len(nums)-1):
            j+=1
            if 0 in nums:
                i=nums.index(0)
                l=i-1
                r=i+1
            else:
                for i in range(nums):
                    if nums[i]>0:
                        r=i
                        l=i-1
                        break
            if j==l:
                l-=1
            if j==r:
                r+=1
            if l>=0 and r<len(nums):
                if nums[j]+nums[l]+nums[r]<0:
                    r+=1
                if nums[j]+nums[l]+nums[r]>0:
                    l-=1
                if nums[j]+nums[l]+nums[r]==0:
                    if [nums[l],nums[j],nums[r]] in l2:
                        continue
                    else:
                        l2.append([nums[l],nums[j],nums[r]])
            if l>=0 and r>=len(nums):
                if nums[j]+nums[l]+nums[r]>0:
                    l-=1
                if nums[j]+nums[l]+nums[r]==0:
                    if [nums[l],nums[j],nums[r]] in l2:
                        continue
                    else:
                        l2.append([nums[l],nums[j],nums[r]])
            if l<0 and r<len(nums):
                if nums[j]+nums[l]+nums[r]<0:
                    r+=1
                if nums[j]+nums[l]+nums[r]==0:
                    if [nums[l],nums[j],nums[r]] in l2:
                        continue
                    else:
                        l2.append([nums[l],nums[j],nums[r]])
            
        return l2
        '''
