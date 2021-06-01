'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Example 4:
Input: nums = [1]
Output: [1]
'''



'''
Logic: We start a decreasing pointer i from the end of the list and we take the i's value before which the list is in ascending 
order. We interchange the values of the list at i-1th index and the one at last index (only if nums[j]>nums[i-1], otherwise
we decrease j's value until the condition is satisfied).
In short we exchange the two largest values on either side of a peak value such that the the largest value after the peak
is larger than the largest value before the peak.
'''
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=j=len(nums)-1
        
        while i>0:
            if nums[i]>nums[i-1]:
                while i<=j and nums[i-1]>=nums[j]:
                    j-=1
                nums[i-1],nums[j]=nums[j],nums[i-1]
                break
            i-=1
        
        nums[i:]=nums[i:][::-1]
                
        
        
        '''
        f=0
        p=len(nums)-2
        if len(nums)<=2:
            nums.reverse()
        else:
            for i in range(len(nums)-2,0,-1):
                if nums[i]>nums[i+1]:
                    continue
                else:
                    if nums[i]<nums[p+1]:
                        nums[i],nums[p+1]=nums[p+1],nums[i]
                    elif nums[i]<nums[p]:
                        nums[i],nums[p]=nums[p],nums[i]
                    else:
                        while(nums[p]<=nums[i]):
                            p-=1
                        nums[i],nums[p]=nums[p],nums[i]
                    f+=1
                    break
            
            if f!=0:
                nums[i+1:]=nums[i+1:][::-1]
            else:
                nums.sort()
        '''

        
        '''
        f=0
        for i in range(len(nums)-1,1,-1):
            for j in range(i-1,0,-1):
                if nums[i]>nums[j]:
                    t=nums[j]
                    nums[j]=nums[i]
                    nums[i]=t
                    f=1
                    p=i
                    q=j
                    break
            if f==1:
                break
        if f==0:
            nums.sort()
        else:
            for i in range(q+1,p):
                for j in range(i+1,p+1):
                    if nums[i]>nums[j]:
                        t=nums[i]
                        nums[i]=nums[j]
                        nums[j]=t
        '''
