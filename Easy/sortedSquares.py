'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''





class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        while(l<r or l==r):             #For reducing the time complexity to O(n/2). 
            if l!=r:
                nums[l]=nums[l]**2
                l+=1
                nums[r]=nums[r]**2
                r-=1
            if l==r:
                nums[l]=nums[l]**2
                l+=1
            
        return sorted(nums)
