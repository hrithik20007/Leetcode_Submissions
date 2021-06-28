'''
Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:
Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
'''



class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        If we find 1 or 0 at i's position, then we look for the opposite bit in the next position. If that is satisfied, then we also check before and after
        them for opposite bits using two pointers and we keep increasing the counter if all conditions are satisfied.
        '''

        c=0
        j=1
        for i in range(0,len(s)-1):
            if s[i]=="0" and s[i+1]=="1":
                c+=1
                while((i-j)!=-1 and (i+1+j)!=len(s) and s[i-j]=="0" and s[i+1+j]=="1"):
                    c+=1
                    j+=1
                j=1
            if s[i]=="1" and s[i+1]=="0":
                c+=1
                while((i-j)!=-1 and (i+1+j)!=len(s) and s[i-j]=="1" and s[i+1+j]=="0"):
                    c+=1
                    j+=1
                j=1   
        return c
