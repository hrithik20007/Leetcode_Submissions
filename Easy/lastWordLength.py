'''
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.
'''

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        else:
            s1=s.strip()
            s2=s1.split(" ")
            l=len(s2)
            s3=s2[l-1]
            l1=len(s3)
            return l1
