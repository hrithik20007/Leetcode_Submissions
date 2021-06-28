'''
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=="":
            return 0
        
        else:
            #A list is created where its length will be 1(the full string itself) or the length may be more if the delimiter is indeed present.
            a=haystack.split(needle)
            if len(a)>1:
                p=len(a[0])
                return p
            else:
                return -1
            
            
