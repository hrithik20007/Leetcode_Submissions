'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red,
white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Example 3:
Input: nums = [0]
Output: [0]

Example 4:
Input: nums = [1]
Output: [1]
'''





class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c=Counter(nums)
        j=0                         #For index
        
        for i in range(3):          #0,1,2
            while c[i]:             #True unless the frequency of the number under consideration is not 0
                nums[j]=i
                c[i]-=1
                j+=1
                
        return nums
        
        
        
        
        '''
        if len(nums)==1:
            return nums
        l=0
        r=len(nums)-1
        while(l<r):
            if nums[l]==0 or nums[r]==2: 
                if nums[l]==0:
                    l+=1
                if nums[r]==2:
                    r-=1
            elif nums[l]>nums[r]:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
            else:
                l+=1
                r-=1
        
        if l==r:
            if nums[l]==0:
                n=nums.index(1)
                nums[l],nums[n]=nums[n],nums[l]
            if nums[l]==2:
                n=nums.index(2,l+1)
                nums[l],nums[n]=nums[n],nums[l]
                
        return nums
        '''
