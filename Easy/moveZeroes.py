'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''



class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums.count(0)==0:
            return nums
        else:
            n1=nums.count(0)
            n2=len(nums)
            n3=n2-n1

            j=0
            for i in nums:  #Inserting all the non-zero numbers at the front of the list  
                if i!=0:
                    nums[j]=i
                    j+=1
                    
            for k in range(n3,n2):  #Filling the remaining length of the list with 0s.
                nums[k]=0
