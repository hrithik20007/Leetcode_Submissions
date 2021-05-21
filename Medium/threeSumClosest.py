'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''




class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==3:
            return sum(nums)

        nums.sort()
        s=sys.maxsize
        
        for i in range(len(nums)-2):
            m=i+1				#Middle pointer. i is left pointer
            r=len(nums)-1		#Right pointer

            while(m<r):
                k=nums[i]+nums[m]+nums[r]
                d=abs(target-k)
                if s>d:
                    s=d
                    p=k
                if k<target:
                    m+=1
                if k>target:
                    r-=1
                if k==target:	#Without this case, it will become an infinite loop if k becomes 0, as none of the other three condition will statisfy and the variables wont change
                    return k

        return p
