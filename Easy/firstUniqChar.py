'''
Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "loveleetcode"
Output: 2

Example 2:
Input: s = "aabb"
Output: -1
'''


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s1=collections.Counter(s)
        s2=[]
        
        for i in s1:    #Appending all unique characters in the string to an array
            if s1[i]==1:
                s2.append(i)

        for j in s:     #Returning the first occurence of a unique character
            if j in s2:
                return s.index(j)
                break
        return -1
    
    
    
        '''
        Another Solution:
        
        for i in s:
            if s.count(i)==1:
                return s.index(i)
                break
        return -1
        '''
        '''
        f=0
        for i in range(0,len(s)-1):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    f+=1
                    continue
            if f==0:
                return i
                break
        if f!=0:
            return -1
                    
        '''
