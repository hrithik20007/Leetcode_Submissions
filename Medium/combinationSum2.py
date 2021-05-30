'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
'''





#Similar to combinationSum
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if sum(candidates)<target:
            return None
        def rec(candidates,k,target,l):
            '''
            if target<0:    #This portion makes the code incredibly slower. So an if statement is used in the for loop instead.
                return
            '''
            if target==0:
                if sorted(l) not in self.sum:
                    self.sum.append(sorted(l))
            else:
                for i in range(k,len(candidates)):
                    if target-candidates[i]>=0:
                        rec(sorted(candidates),i+1,target-candidates[i],l+[candidates[i]])
        
        self.sum=[]
        rec(sorted(candidates),0,target,[])
        return self.sum
