/*
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.
Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 
column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

Example 1:
Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2

Example 2:
Input: board = [["."]]
Output: 0
*/






//Logic: If we have no "X" before a row or column, we increase the counter by 1.
/**
 * @param {character[][]} board
 * @return {number}
 */
var countBattleships = function(board) {
    var i,j,c=0;
    for(i=0;i<board.length;i++){
        for(j=0;j<board[0].length;j++){
            if(board[i][j]=="X" && (j==0 || board[i][j-1]==".") && (i==0 || board[i-1][j]=="."))
                c+=1;
        }
    }
    
    return c;
};
