'''
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
'''





class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l=[]
        n=len(nums)
        for i in range(2**n):               #The no. of subsets is 2**n [Valued as 0 to 2**n-1 in binary representation for the subsets; here 000 represents []
                                            #and 111 represents the last subset]. 
            l1=[]
            for j in range(n):              #For getBit. Only those positional elements are appended where the bit is 1.
                if(i & 1<<j):
                    l1.append(nums[j])
            l.append(l1)
            
        return l
