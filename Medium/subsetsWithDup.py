'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
'''




#It is same as subsets.py .I have only added an if statement to check for dupliactes before appending the sorted sublists into the answer list.
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        l=[]
        n=len(nums)
        for i in range(2**n):
            l1=[]
            for j in range(n):
                if(i & 1<<j):
                    l1.append(nums[j])
            
            if sorted(l1) not in l:
                l.append(sorted(l1))
            
        return l
