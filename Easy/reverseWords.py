'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
'''




class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1=s.split(" ")
        for i in range(0,len(s1)):
            s1[i]=s1[i][::-1]
            
        s2=' '.join(s1)
        return s2
