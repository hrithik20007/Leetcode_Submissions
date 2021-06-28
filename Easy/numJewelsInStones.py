'''
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0
'''




class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        s=0
        j=list(jewels)
        for i in j:
            s+=stones.count(i)
            
        return s
        '''
        This is correct but I wanted a faster solution
        
        
        c=0
        j=list(jewels)
        for i in stones:
            if i in j:
                c+=1
                
        return c
        '''
