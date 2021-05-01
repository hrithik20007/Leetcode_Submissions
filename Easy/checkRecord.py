'''
You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. 
The record only contains the following three characters:
    'A': Absent.
    'L': Late.
    'P': Present.

The student is eligible for an attendance award if they meet both of the following criteria:
    The student was absent ('A') for strictly fewer than 2 days total.
    The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.

Example 1:
Input: s = "PPALLP"
Output: true
Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
'''




class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=s.count('A')
        for i in range(0,len(s)):
            if s[i]=='L' and i!=len(s)-1 and i!=len(s)-2:   #Making sure the L is not second last or last character in which case there cannot be 3 consecutive 'L's.
                if s[i+1]=='L' and s[i+2]=='L':
                    return False
        
        if a>=2:
            return False
        else:
            return True
                    
