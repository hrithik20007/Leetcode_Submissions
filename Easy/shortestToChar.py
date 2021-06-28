'''
Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.
The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

Example 1:
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 3.
For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.

Example 2:
Input: s = "aaab", c = "b"
Output: [3,2,1,0]
'''



class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        l=[]
        a=[]
        j=0
        for i,v in enumerate(s):
            if v==c:
                l.append(i)     #Holds the indexes of all the occurences of the character c
                
        for i,v in enumerate(s):    #i holds the index while v holds the value
            if v==c:
                a.append(0)
                j+=1
            elif i<l[0]:        #If the index of the current iteration is less than the index of first occurence of c.
                a.append(l[0]-i)
            elif i>l[-1]:       #If the index of the current iteration is more than the index of last occurence of c.
                a.append(i-l[-1])
            else:
                a.append(min(l[j]-i,i-l[j-1]))  #If the index of the current iteration is between the indexes of the first and last occurences of c.
                
        return a



        
        '''
        This is correct but I want a faster solution
        
        
        l=[]
        for i in range(len(s)):
            j1=0                        #First pointer which will move to the right and increase by 1 until c is found
            j2=0                        #Second pointer that will move to the left and increase by 1 until c is found
            i1=i                        #index of the first pointer
            i2=i                        #index of the second pointer
            while s[i1]!=c and s[i2]!=c:
                if i2<=len(s)-2:
                    j2+=1
                    i2+=1
                if i1>=1:
                    j1+=1
                    i1-=1
                    
            if s[i1]==c:
                l.append(j1)
            elif s[i2]==c:
                l.append(j2)
            elif s[i1]==c and s[i2]==c:
                l.append(j1)
                
        return l
        '''
