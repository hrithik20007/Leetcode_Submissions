'''
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"
'''





class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==1 or len(s)==len(list(set(list(s)))):
            return s[0]
        i=0
        m=0
        while(i<len(s)):
            l=i-1
            r=i+1
            while(r<len(s) and s[r]==s[i]):  #Only increases the right pointer if the elements are same. Like if i is at the first 'm', then for "ammmc", the r will increase until c (since, it exits after r+1).
                r+=1
            while(l>=0 and r<len(s) and s[l]==s[r]):  #If the next element is different from the one at i. Example - abcba.. if i is at 'c'.
                l-=1
                r+=1
            if (r-l)>m:    #Sees that r is updated only if the length is greater than the previous cases; else ignores.
                m=r-l
                s1=s[l+1:r]    #As l is decreased one extra time and r is increased one extra time before leaving the while loop.
            i+=1
        return s1




    '''
    Again correct, but time limit exceeds
    
    
    def palindrome(self,s1):
        i=0
        j=len(s1)-1
        while(i<j):
            if s1[i]!=s1[j]:
                return False
            i+=1
            j-=1
        return True
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l1=[]
        if len(s)==1 or len(s)==len(list(set(list(s)))):
            return s[0]
        for i in range(0,len(s)):
            l=i-1
            r=i+1
            while(l>=0 and r<=len(s)-1):
                st1=s[l:r+1]
                st2=s[l:i+1]
                st3=s[i:r+1]
                if self.palindrome(st1):
                    l1.append(st1)
                if self.palindrome(st2):
                    l1.append(st2)
                if self.palindrome(st3):
                    l1.append(st3)
                l-=1
                r+=1
        if len(l1)==0:
            return s[0]
        else:
            l1.sort(key=len)
            return l1[-1]
    '''




    
    '''
    This works but time limit exceeded
    
    
    def palindrome(self,s1):
        i=0
        j=len(s1)-1
        while(i<j):
            if s1[i]!=s1[j]:
                return False
            i+=1
            j-=1
        return True
            
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=[]
        if len(s)==1 or len(s)==len(list(set(list(s)))):
            return s[0]
        for i in range(0,len(s)-1):
            for j in range(1,len(s)):
                st=s[i:j+1]
                if self.palindrome(st):
                    l.append(st)
                    
        l.sort(key=len)
        return l[-1]
    '''





    
    '''
    def palindrome(self,s1):
        i=0
        j=len(s1)-1
        while(i<j):
            if s1[i]!=s1[j]:
                return False
            i+=1
            j-=1
        return True
            
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==1 or len(s)==len(list(set(list(s)))):
            return s[0]
        f=0
        l=[]
        st=s[:]
        while(len(st)>=2):
            if self.palindrome(st):
                l.append(st)
                f+=1
                break
            else:
                st=st[:len(st)-1]
        f+=1
        
        st=s[:]
        while(len(st)>=2):
            if self.palindrome(st):
                l.append(st)
                f+=1
                break
            else:
                st=st[1:]
        f+=1
        
        st=s[:]
        while(len(st)>=2):
            if self.palindrome(st):
                l.append(st)
                f+=1
                break
            else:
                st=st[1:len(st)-1]
        f+=1
        
        if f==3:
            return False
        else:
            l.sort(key=len)
            return l[-1]
    '''
