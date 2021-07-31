'''
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.

Example 1:
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
'''






'''
Logic: We are appending the minimum of two's, three's and five's multiples in each iteration and then increase the pointer which pointed to that minimum such that it
now points to the next smallest option possible (other than the previous three). We repeat the process and append the minimum numbers to nums. When nums reaches size
n, then we return the last number. 
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums=[1]
        
        two=0
        three=0
        five=0
        
        while(len(nums)<n):
            m2=nums[two]*2
            m3=nums[three]*3
            m5=nums[five]*5
            
            l=min(m2,m3,m5)
            nums.append(l)
            if l==m2:
                two+=1
            if l==m3:
                three+=1
            if l==m5:
                five+=1
                
        return nums[-1]
        
        
        

        
        '''
        Time Limit Exceeds
        
        

        l=[]
        i=1
        c=0
        while(True):
            j=i
            while(j%2==0 or j%3==0 or j%5==0):
                while j%5==0:
                    j=j/5
                while j%3==0:
                    j=j/3
                while j%2==0:
                    j=j/2

            if j==1:
                l.append(i)
                c+=1
                if c==n:
                    return l[-1]
            i+=1
        '''
