'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
'''





class Solution(object):

    def left(self,nums,target,left,right):      #For the leftmost index (called after target is found in the first function)
        while(left<right):                      #We have not done less than EQUAL TO for cases like [1],1.
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]==target and nums[mid-1]<target:
                return mid
            elif nums[mid]==target and not nums[mid-1]<target:
                right=mid-1
        return left
        
    def right(self,nums,target,left,right):     #For the rightmost index (called after target is found in the first function)
        while(left<right):                      #We have not done less than EQUAL TO for cases like [1],1.
            mid=(left+right)//2
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]==target and nums[mid+1]>target:
                return mid
            elif nums[mid]==target and not nums[mid+1]>target:
                left=mid+1
        return right
        
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=0
        h=len(nums)-1
        while(l<=h):
            mid=(l+h)//2
            if nums[mid]>target:
                h=mid-1
            if nums[mid]<target:
                l=mid+1
            if nums[mid]==target:
                return [self.left(nums,target,0,mid),self.right(nums,target,mid,h)] 
            
        return [-1,-1]      #In case, the indexes do not exist
    
    
    
    
        '''
        l1=[]
        l=0
        h=len(nums)-1
        while(l<h):
            mid=(l+h)//2
            if nums[mid]>target:
                h=mid-1
            if nums[mid]<target:
                l=mid+1
            if nums[mid]==target:
                l1.append(mid)
                if target in nums[:mid]:
                    h=mid
                    l=0
                if target in nums[mid+1:]:
                    l=mid
                    h=len(nums)
        '''
