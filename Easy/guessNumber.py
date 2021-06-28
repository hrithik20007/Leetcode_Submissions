'''
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:
    -1: The number I picked is lower than your guess (i.e. pick < num).
    1: The number I picked is higher than your guess (i.e. pick > num).
    0: The number I picked is equal to your guess (i.e. pick == num).

Return the number that I picked.
'''




# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=1
        h=n
        mid=(l+h)//2
        while(guess(mid)!=0):
            if guess(mid)==-1:
                h=mid-1
            elif guess(mid)==1:
                l=mid+1
            mid=(h+l)//2
            
        return mid
        '''
        Time Limit Exceeds for large ranges
        
        
        pick=random.randint(1,n)
        while(guess(pick)!=0):
            if guess(pick)==1:
                pick+=1
            elif guess(pick)==-1:
                pick-=1
        return pick
        '''
