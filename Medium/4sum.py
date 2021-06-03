'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''




#Function Path --> fourSum -> getsum (until two elements remain in nums)-> twoSum -> getsum -> return
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def twoSum(nums, target):
            left = 0
            right = len(nums) - 1
            result = []

            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([nums[left], nums[right]])

                    current = nums[left]
                    while left < right and current == nums[left]:   #So that same number is not repeated
                        left += 1

                    current = nums[right]
                    while left < right and current == nums[right]:  #So that same number is not repeated
                        right -= 1

                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
            return result


        def getSum(nums, target, order):
            result = []
            if order == 2:
                return twoSum(nums, target)
            if order > 2:
                index = 0
                while index < len(nums):
                    lists = getSum(nums[index + 1:], target - nums[index], order - 1)
                    for j in lists:
                        result.append([nums[index]] + j)

                    current = nums[index]
                    while index < len(nums) and current == nums[index]:     #So that same number is not repeated
                        index += 1
            return result
        
        return getSum(sorted(nums), target, 4)
        
        
        
        
        '''
        s=[]
        s1=[]
        l1=[]
        if len(nums)<4:
            return []
        if len(nums)==4:
            if sum(nums)==target:
                return [nums]
            else:
                return []
        nums.sort()
        def threesum(nums,target):
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                l=i+1
                r=len(nums)-1
                while(l<r):
                    k=nums[i]+nums[l]+nums[r]
                    if k>target:
                        r-=1
                    elif k<target:
                        l+=1
                    else:
                        l1.append([nums[i],nums[l],nums[r]])
                        l+=1
                        while(l<r and nums[l]==nums[l-1]):
                            l+=1
            return l1

        index = 0
        while index < len(nums):
            tuples = threesum(nums[index + 1:], target - nums[index])
            for tup in tuples:
                s.append([nums[index]] + tup)

            current = nums[index]
            while index < len(nums) and current == nums[index]:
                index += 1
        return s
        '''
