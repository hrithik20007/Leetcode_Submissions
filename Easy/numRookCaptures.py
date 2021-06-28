'''
On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', black pawns 'p', and empty squares '.'.
When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that direction until it chooses to stop, reaches the 
edge of the board, captures a black pawn, or is blocked by a white bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's turn. 
The number of available captures for the white rook is the number of pawns that the rook is attacking.
Return the number of available captures for the white rook.

Example 1:
Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: In this example, the rook is attacking all the pawns.

Example 2:
Input: board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation: The bishops are blocking the rook from attacking any of the pawns.

Example 3:
Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: The rook is attacking the pawns at positions b5, d6, and f5.
'''





class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        f=0
        c=0
        lr=[]
        lc=[]
        for i in range(len(board)):                 #This nested loop finds the position of R and stores i,j as m,n.
            for j in range(len(board[0])):
                if board[i][j]=="R":
                    m=i
                    n=j
                    f=1         
                    break
            if f==1:
                break
                
        for i in range(len(board)):                 #Makes a list of all the non empty plces in the same column as R.
            if board[i][n]!='.':
                lc.append(board[i][n])
        
        for j in range(len(board[0])):              #Makes a list of all the non empty plces in the same row as R.
            if board[m][j]!='.':
                lr.append(board[m][j])
        
        for i in range(len(lc)):                    #If the pieces in the immideate up or down is 'p', then count increases by 1
            if lc[i]=='R':
                if i-1>=0 and lc[i-1]=='p':
                    c+=1
                if i+1<len(lc) and lc[i+1]=='p':
                    c+=1
        
        for i in range(len(lr)):                    #If the pieces in the immideate left or right is 'p', then count increases by 1
            if lr[i]=='R':
                if i-1>=0 and lr[i-1]=='p':
                    c+=1
                if i+1<len(lr) and lr[i+1]=='p':
                    c+=1
        
        return c
    
    

    
    
        '''
        Works but slow
        
        
        
        f=0
        c=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="R":
                    m=i
                    n=j
                    f=1         
                    break
            if f==1:
                break
        
        p=m
        q=n
        
        q-=1
        while(q>=0):
            if board[m][q]!='.':
                if board[m][q]=='B':
                    break
                else:
                    c+=1
                    break
            q-=1
                   
        q=n+1
        while(q<len(board[0])):
            if board[m][q]!='.':
                if board[m][q]=='B':
                    break
                else:
                    c+=1
                    break
            q+=1
            
        
        
        p-=1
        while(p>=0):
            if board[p][n]!='.':
                if board[p][n]=='B':
                    break
                else:
                    c+=1
                    break
            p-=1
                   
        p=m+1
        while(p<len(board)):
            if board[p][n]!='.':
                if board[p][n]=='B':
                    break
                else:
                    c+=1
                    break
            p+=1
            
        return c
        '''
