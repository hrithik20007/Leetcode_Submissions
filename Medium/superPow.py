'''
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example 1:
Input: a = 2, b = [3]
Output: 8

Example 2:
Input: a = 2, b = [1,0]
Output: 1024

Example 3:
Input: a = 1, b = [4,3,3,8,5,2]
Output: 1

Example 4:
Input: a = 2147483647, b = [2,0,0]
Output: 1198
'''




'''
Logic: 
This program is based on Euler's Theorem which states that: a^( phi(n) ) = 1 (mod n), where phi(n) is Euler's Totient Function, provided that a and n are relatively 
prime (meaning they have no common factors). In our case, n = 1337, which has prime factorization 1337 = 7 x 191. We know that phi(p) = p - 1 when p is prime and 
also that phi(p x q) = phi(p) x phi(q). Thus it follows that phi(1337) = phi(7 x 191) = phi(7) x phi(191) = 6 x 190 = 1140. Thus, using Euler's Theorem it follows 
that a^1140 = 1 (mod 1337), provided that a and 1337 have no common factors. Since 1337 only has two factors, 7 and 191, it follows that a^1140 = 1 (mod 1337), 
provided that a is not divisible by 7 or 191.

First step is to extract exponent from input parameter b, either by string operation, or reduce with lambda.
Second step is to compute power with speed up by Euler theorem
For more detailed demo and illustration, please refer to this article by @ShuangquanLi

Let exp denote the exponent extracted from input b

Goal = (a ^ exp) mod 1337
= a ^ ( exp mod φ(1337) ) mod 1337
= a ^ ( exp mod 1140) mod 1337
use the formula derived above to reduce computation loading and to have higher performance.

Remark:
φ( 1337 )
= φ( 7 x 191 ) where 7 and 191 are prime factor of 1337's factor decomposition
= φ( 7 ) x φ( 191 )
= ( 7 - 1 ) x ( 191 - 1 )
= 6 x 190
=1140

Euler's totient function φ( n ) counts the positive integers up to a given integer n that are relatively prime to n
'''
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if a==1 or a==0:
            return a
        
        d=0
        for i in b:
            d=d*10+i;

        d=d%1140;
        return pow(a,d,1337)
