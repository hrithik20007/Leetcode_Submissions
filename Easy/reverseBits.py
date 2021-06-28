'''
Reverse bits of a given 32 bits unsigned integer.

Note:
    Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
    In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.

Follow up:
If this function is called many times, how would you optimize it?
'''



class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n1=bin(n)[2:]
        if len(n1)<32:

            '''
            We could have also done n1=n1.zfill(32) instead of the if statement. zfill(n) pads the left side of a string with "0"s until the length totals to n.
            When we pass a binary like 000101 as an integer, python starts reads it as 101 ignoring the first 3 zeros. That's why we need zfill().
            A binary is written as 0bxxx, then only the zeroes in the front remain intact(if any). When we print such a value, it directly prints the 
            decimel equivalent of that binary number.
            '''
            n1="0"*(32-len(n1))+n1
        n2="0b"+n1[::-1]  #To convert it into a binary (in the string format).
        n3=int(n2,2)  #Converts the binary to an integer. Actually, it takes a string as first aurgument and a base as second. Base 2 would give 4 for '100'. Base 8 would have given 64 for the same.
        return n3
