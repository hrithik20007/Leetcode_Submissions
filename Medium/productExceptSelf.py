'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''





'''
Logic: Basically we are multiplying all numbers cumulatively in the array and then in the oppposite order, such that a particular index will show all the numbers
multiplied before it * multiplication of all the numbers after it. Below solution will help more in clarifying, as it is from the same concept. But there, we utilised
two extra arrays whereas here we implemented the logic in a single array.
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]*(len(nums))
        
        prefix=1
        for i in range(len(nums)):
            ans[i]=prefix
            prefix*=nums[i]
            
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=postfix
            postfix*=nums[i]
        
        return ans
        
        
        
        
        
        '''
        Works but TLE




        prefix=[nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1]*nums[i])
        prefix=[1]+prefix

        postfix=[nums[-1]]
        for i in range(len(nums)-2,-1,-1):
            postfix=[postfix[0]*nums[i]]+postfix
        postfix.append(1);


        ans=[]
        for i in range(1,len(prefix)):
            ans.append(prefix[i-1]*postfix[i])

        return ans
        '''
