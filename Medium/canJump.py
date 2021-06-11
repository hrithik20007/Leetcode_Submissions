'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
'''




class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m=0
        r=len(nums)-1
        for i in range(r):          #Iterates until the second last element
            if m<i:
                return False
            else:
                m=max(m,i+nums[i])  #We do not update even for later i's beacuse unless i+nums[i] is greater than the current m, because their maximum leap will
                                    #either converge or fall short of m's maximum leap
                
        if m>=r:                    #Comparing for the last index
            return True
        else:
            return False
        
        
        
        '''
        def jump(nums):
            if len(nums)==1:
                return 1
            if nums[0]==0:
                return 0
            for i in range(1,nums[0]+1):
                r=jump(nums[i:])
                if r==1:
                    return True

            return False
        
        return jump(nums)
        '''
