'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false
'''




class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #Using two pointers

        i=0
        j=len(s)-1
        while(i<j):
            if (s[i]!=s[j]):
                a=s[:i]+s[i+1:]     #We used slicing method to cut the specific character instead of replace() because in replace it is harder if the characters occurs multiple times.
                b=s[:j]+s[j+1:]
                if a==a[::-1] or b==b[::-1]:    #The anomaly may be at the i-th index or j-th index, so we check for both the cases.
                    return True
                    break
                else:
                    return False
                    break
            i+=1
            j-=1
            
        return True     #If the whole while statement is passed without encountering any anomaly that means only the middle character remains and the word will be 
                        #palindrome regardless of what it is
    

        '''
        Time Limit Exceeded
        
        
        for i in range(0,len(s)):
            a=s[:i]+s[i+1:]
            if a==a[::-1]:
                return True
                break

        return False
        '''
