'''
Given an array nums of non-negative integers, return an array consisting of all the even elements of nums, followed by all the odd elements of nums.
You may return any answer array that satisfies this condition.

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
'''




#Both solutions work and nearly take the same time
lass Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        while(l<r):
            if nums[l]%2==0:
                l+=1
            else:
                nums[l],nums[r]=nums[r],nums[l]
                r-=1
                
        return nums

#==============================OR=======================================

        l1=[]
        l2=[]
        for i in nums:
            if i%2==0:
                l1.append(i)
            else:
                l2.append(i)
                
        return l1+l2
