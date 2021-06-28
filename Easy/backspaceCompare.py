'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a##c", t = "#a#c"
Output: true
Explanation: Both s and t become "c".

Example 4:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
'''





class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1=[]
        l2=[]
        
        for i in s:     #Modifies s
            if i!='#':
                l1.append(i)
            else:
                if len(l1)!=0:
                    l1.pop()
                    
        for i in t:    #Modifies t
            if i!='#':
                l2.append(i)
            else:
                if len(l2)!=0:
                    l2.pop()
                    
        s1=''.join(l1)
        s2=''.join(l2)
        if s1==s2:
            return True
        else:
            return False
