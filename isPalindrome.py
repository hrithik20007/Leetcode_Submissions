#Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1=""
        for i in s:
            #isalnum checks for alphanumeric characters only (either alphabet or a number)
            if i.isalnum():
                s1=s1+i
                
        s1=s1.lower()
        s2=s1[::-1]
        if(s1==s2):
            return True
        else:
            return False
