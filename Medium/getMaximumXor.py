'''
You are given a sorted array nums of n non-negative integers and an integer maximumBit. You want to perform the following query n times:
    Find a non-negative integer k < 2maximumBit such that nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k is maximized. k is the answer to the ith query.
    Remove the last element from the current array nums.
Return an array answer, where answer[i] is the answer to the ith query.

Example 1:
Input: nums = [0,1,1,3], maximumBit = 2
Output: [0,3,2,3]
Explanation: The queries are answered as follows:
1st query: nums = [0,1,1,3], k = 0 since 0 XOR 1 XOR 1 XOR 3 XOR 0 = 3.
2nd query: nums = [0,1,1], k = 3 since 0 XOR 1 XOR 1 XOR 3 = 3.
3rd query: nums = [0,1], k = 2 since 0 XOR 1 XOR 2 = 3.
4th query: nums = [0], k = 3 since 0 XOR 3 = 3.
'''




'''
Logic: 
When a^b=c, then a^c=b
Why? Because-
=> a^a^b^=a^c
=> 0^b=a^c 
=> b=a^c (We know, 0^b=b)

Thus, instead of striving to acheive the maximum no. by XOR-ing with k, we XOR with the maximum no. to find the required value of k. (i.e. in our logic example,
replace b with k and c with maximum no. and then think about it).

Also, notice that the maximum no. is always (2**maximumBit)-1. Thus, we already know what maximum value we will get. Actually, c will always be = abs(b-a).
'''
class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        k=(2**maximumBit)-1
        l=[]
        t=nums[0]
        l.append(t^k)
        for i in range(1,len(nums)):
            t=t^nums[i]
            l.append(t^k)
        return l[::-1]
        '''
        Time Limit Exceeded

        
        l=[]
        r=-1
        while(len(nums)!=0):
            for k in range(0,2**maximumBit):
                xor1=reduce(ixor,nums)      #By this method, we can calculate bitwise XOR of any list elements
                xor2=xor1^k
                if r<xor2:
                    r=xor2
                    c=k
            l.append(c)
            r=-1
            nums.pop()
        
        return l       
        '''
