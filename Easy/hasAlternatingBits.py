'''
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101

Example 2:
Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.
'''


#In case of C++, we can use checkBit method to check if the bit is 1 or 0 by left shifting 1 after each iteration

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=bin(n)
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                return False
            
        return True
