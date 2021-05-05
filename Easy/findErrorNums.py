'''
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:
Input: nums = [1,1]
Output: [1,2]
'''




class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r=[]
        l=list(set(nums))
        
        r.append(sum(nums)-sum(l))     #Appends the repeting no.
        r.append(list(set(list(range(1,len(nums)+1)))-set(nums))[0])    #Appends the missing no.
        
        return r
        
        '''
        This is my solution and it works but I wanted a faster solution.

        
        r=[]
        l=list(set(nums))
        
        c=Counter(nums)
        for i in l:     #We could also just use c or c.keys in place of l.(For the repeating no.)
            if c[i]==2:
                r.append(i)
        
        for i in range(1,len(nums)+1):  #(For the missing no.)
            if i not in nums:
                r.append(i)
                
        return r
        '''
