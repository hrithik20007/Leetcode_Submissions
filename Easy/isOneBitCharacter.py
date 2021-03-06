'''
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).
Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.

Example 2:
Input: 
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
'''




class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        #Return True if the last one is a 1-bit character else False
        
        
        i=0
        while(i<=len(bits)-1):
            if bits[i]==1:
                i+=2
                if i==len(bits):
                    return False
            else:
                i+=1
                
        return True
        '''
        This is my solution and it works but I wanted a faster solution
        
        
        while(len(bits)>=2):
            if bits[0]==0:
                bits=bits[1:]
            else:
                bits=bits[2:]
            
        if len(bits)==0:
            return False
        else:
            return True
        '''
