'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s1={}
        t1={}
        si=0
        ti=0
        
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                
                #Working on the logic that in case of isomorphic strings, new characters occur at the same indices
                if s[i] not in s1:
                    s1[s[i]]=si
                    si+=1
                if t[i] not in t1:
                    t1[t[i]]=ti
                    ti+=1
                    
                #Checking whether the indices for each new charcaters match    
                if s1[s[i]]!=t1[t[i]]:
                    return False
            return True
                
        '''
        if s==t:
            return True
        else:
            s1={}
            s2=[]
            t1=list(t)
            f=0
            c=0
            for j in s:
                if j not in s2:
                    s2.append(j)
            for i in s:
                if i not in s1:
                    s1[i]=t1[f]
                else:
                    if t1[f]==s1[i]:
                        c+=1
                    else:
                        return False
                f+=1

                if len(s)-len(s2)==c:
                    return True
        '''
