'''
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
Return any answer array that satisfies this condition.

Example 1:
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Example 2:
Input: nums = [2,3]
Output: [2,3]
'''





class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        le=[]
        lo=[]
        ans=['a']*len(nums)
        for i in range(len(nums)):
            if nums[i]%2==0:
                le.append(nums[i])
            else:
                lo.append(nums[i])
                
        ans[::2]=le
        ans[1::2]=lo
                
        return ans
        
        
#BOTH THE SOLUTIONS GIVEN BELOW WORK, BUT THEY ARE A BIT SLOWER                
        '''
        le=[]
        lo=[]
        ans=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                le.append(nums[i])
            else:
                lo.append(nums[i])
                
        for i in range(0,len(nums)-1,2):
            ans.append(le.pop(0))
            ans.append(lo.pop(0))
                
        return ans
        '''
        
        
        
        
        '''
        for i in range(len(nums)):
            if i%2==0:
                if nums[i]%2==0:
                    continue
                else:                                   #If an odd number is even found at even position, a while loop is increamented until an even no. is found
                                                        #with which the current no. is replaced.
                    j=i+1
                    while(nums[j]%2!=0):
                        j+=1
                    nums[i],nums[j]=nums[j],nums[i]
                    
            else:
                if nums[i]%2!=0:
                    continue
                else:                                   #Same as above, but in case of odd number
                    j=i+1
                    while(nums[j]%2==0):
                        j+=1
                    nums[i],nums[j]=nums[j],nums[i]
                    
        return nums
        '''
