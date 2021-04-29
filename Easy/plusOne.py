'''
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        new=[]
        s=""
        
        #Store the list as a string s
        for i in digits[:]:
            s=s+str(i)

        k=int(s)
        k1=k+1
        s2=str(k1)
        
        #Change a string into a list (2 methods are provided)
        new=list(s2)
        #or new[:0]=s2

        '''
        p=0
        for j in s2:
            print(j)
            print("------------")
            new[p]=int(j)
            p=p+1
        '''        
        return new

            
