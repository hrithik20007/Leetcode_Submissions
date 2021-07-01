'''
Alice and Bob take turns playing a game, with Alice starting first.
Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:
    Choosing any x with 0 < x < n and n % x == 0.
    Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.
Return true if and only if Alice wins the game, assuming both players play optimally.

Example 1:
Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.

Example 2:
Input: n = 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
'''





class Solution:
    def divisor(self,n,x):
        if n==1 and x%2==0:
            return False
        elif n==1 and x%2==1:
            return True
        
        for i in range(1,n):
            if n%i==0:
                return self.divisor(n-i,x+1)        #Looks at all possible moves possible and returns True if any one works (this is not optimal).
    
    def divisorGame(self, n: int) -> bool:
        return self.divisor(n,0)                    #We send 0 to keep track of moves by A or B. If the final number is even, that means A couldn't make his move
                                                    #and he lost, while odd would mean B couldn't make his final move and A won.
