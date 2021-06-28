'''
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

Example 1:
Input: nums = [2,1,2]
Output: 5

Example 2:
Input: nums = [1,2,1]
Output: 0

Example 3:
Input: nums = [3,2,3,4]
Output: 10

Example 4:
Input: nums = [3,6,2,3]
Output: 8
'''





class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        r=len(nums)-1                               #Stores the largest no.
        m=len(nums)-2
        l=len(nums)-3                               #Stores the smallest no.
        
        if nums[r]>=(nums[m]+nums[l]):              #To form a triangle, the largest side should be smaller than the sum of the two shorter sides
            l-=1
            m-=1
            r-=1
            while(l>=0):                            #The lengths are reduced to see if the condition is met eventually, otherwise returns 0
                if nums[r]>=(nums[m]+nums[l]):
                    l-=1
                    m-=1
                    r-=1
                else:
                    break
                    
            if l==-1:                               #Condition is not met for any of the available lengths
                return 0
            else:
                return nums[l]+nums[m]+nums[r]

        else:
            return nums[l]+nums[m]+nums[r]
