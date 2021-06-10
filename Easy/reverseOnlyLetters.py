'''
Given a string s, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 1:
Input: s = "ab-cd"
Output: "dc-ba"

Example 2:
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
'''





class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l=[]
        d={}
        for i in range(len(s)):
            if s[i].isalpha():
                l.append(s[i])      #Appends alphabets to a list
            else:
                d[i]=s[i]           #Appends non-alphabets to a dictionary as values and their indexes as keys
        
        l=l[::-1]
        
        r=['a']*len(s)              #Result list initialised
        j=0
        for i in range(len(r)):
            if i not in d.keys():   #If i is an alphabet
                r[i]=l[j]
                j+=1
            else:                   #If i is not an alphabet
                r[i]=d[i]
                
        return ''.join(r)            
