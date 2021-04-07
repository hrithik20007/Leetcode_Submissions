'''
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:
1)Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
2)In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3 (i.e. "11111111111111111111111111111101").
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
'''
bin() converts an integer into its binary equivalent string. 
[:2] helps us omit the '0b' at the beginning 
(0b is how python tells us what the bse number is. 0b stands for base2, 0x stands for base16, 0. stands for base8). 
count() takes a string as parameter and searches it in a list or string.
'''
        n1=bin(n)[2:].count("1")
        return n1
        '''
        f=0 
        
        n1=str(n)
        for i in n1:
            if i=='1':
                f+=1
                
        return f
        '''            
