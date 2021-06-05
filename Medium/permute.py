'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
'''



'''
                                                                            Logic:

                                                                          1   2    3
                                                                        / |   | \   \ \
                                                                      12  13  21 23  31 32
                                                                      /   |   |   \    \   \ 
                                                                    123  132 213  231  312 321 
                                                                                                             
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutation(nums,n1,ans,l):
            if len(l)==len(n1):
                ans.append(l[:])
                return
            
            for i in range(len(n1)):
                if n1[i]==True:         #Skips the characters currently under consideration
                    continue
                n1[i]=True              #We write these two lines instead of writing them directly in the function parameters as it assigns them like--
                                        #l=l.append(n[i]) and this l becomes a none type instead of a list as append does not return any new list
                l.append(nums[i])
                permutation(nums,n1,ans,l)
                n1[i]=False
                l.pop()
                
        ans=[]
        permutation(nums,[False]*len(nums),ans,[])
        
        return ans
        
        

        
        '''
        Fastest but depends on python function
        
        
        l=[]
        n=permutations(nums)
        for i in list(n):
            l.append(list(i))
            
        return l
        '''
        

        
        '''
        def permutation(nums,n1,ans,l):
            if len(l)==len(nums):
                ans.append(l[:])
                return
            for i in range(len(n1)):
                if len(n1)==0:
                    return
                l.append(n1[i])
                n1.pop(i)
                permutation(nums,n1,ans,l)
                l.pop()
                n1.append(n1[i])
                
        ans=[]
        n1=nums[:]
        permutation(nums,n1,ans,[])
        return ans
        '''
