'''
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.
Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].
    For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

Example 1:
Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

Example 2:
Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

Example 3:
Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

Example 4:
Input: s = "aaaaaaabc", goal = "aaaaaaacb"
Output: true
'''





class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        l=[]
        if len(s)!=len(goal):
            return False
        if len(set(s))<len(s) and s==goal:  #For cases similar to example 3
            return True
            
        for i in range(len(s)):
            if s[i]!=goal[i]:
                if len(l)<=1:
                    l.append(i)
                else:
                    return False
                
        if len(l)!=2:       #For a single swap, there must only be two places where the strings differ
            return False
        if goal[l[0]]==s[l[1]] and goal[l[1]]==s[l[0]]:
            return True
