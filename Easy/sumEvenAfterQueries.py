'''
We have an array nums of integers, and an array queries of queries.
For the i-th query val = queries[i][0], index = queries[i][1], we add val to nums[index].  Then, the answer to the i-th query is the sum of the even values of A.
(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array nums.)
Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.

Example 1:
Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation: 
At the beginning, the array is [1,2,3,4].
After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
'''





class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        l=[]
        s=sum([i for i in nums if i%2==0])

        for i in range(len(queries)):
            n=nums[queries[i][1]]
            if n%2==0:                                              #If the number is odd, it won't be a part of the sum in the first place. We remove this from sum
                                                                    #because it's value is about to change.
                s=s-n

            nums[queries[i][1]]=nums[queries[i][1]]+queries[i][0]
            if nums[queries[i][1]]%2==0:                            #If the changed value is even, only then is it added back to the sum.
                s=s+nums[queries[i][1]]
            l.append(s)

        return l
