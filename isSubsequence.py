'''
Given two strings s and t, check if s is a subsequence of t.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
'''



class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1=list(s)

        '''
        As soon as we get a match in the first index, it is removed and if the chracters' chronology is followed then by the end of the for loop, the list becomes 
        empty. The if statement of length check is written before the elif because in case of vice-versa where the index position is checked, if the loop becomes
        empty before the for loop ends, then the if statement will throw an error of list index out of range as in an empty list, s1[0] does not exist.

        We have avoided statment like 'if i in s1 and i!=s1[0]' because even in chronological cases a repeating word may not lie in s1[0].
        '''
        for i in t:
            if len(s1)==0:
                break
            elif i==s1[0]:
                s1.remove(i)
        
        if len(s1)==0:
            return True
        else:
            return False
                
