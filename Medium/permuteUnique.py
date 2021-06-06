'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''



#Same as permutation, but with an extra if statement to check for unique permutations.
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permute(nums,l,n1,ans):
            if len(l)==len(nums):
                if l[:] not in ans:
                    ans.append(l[:])
                return
            for i in range(len(n1)):
                if n1[i]==True:
                    continue
                n1[i]=True
                l.append(nums[i])
                permute(nums,l,n1,ans)
                n1[i]=False
                l.pop()
            
        ans=[]    
        permute(nums,[],[False]*len(nums),ans)
        
        return ans
