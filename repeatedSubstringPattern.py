'''
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false
'''


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n1=len(s)
        n=len(s)//2     #A substring length must be half of the original string at most, if we are to reproduce the original string from that substring. 
        
        for i in range(1,n+1):
            s1=s[0:i]   #s1 produces a new substring with increasing characters (all always starting from the 0th position) with each iteration.
            n2=len(s1)
            
            if n1%n2==0:    #The length of the original string must be a multiple of the substring.
                n3=n1//n2
                s2=s1*n3    #s2 stores the new string produced by repeating the substring s1.
                if s2==s:
                    return True
                
        return False
