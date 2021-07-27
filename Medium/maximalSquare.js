/*
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0
*/






/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function(matrix) {
    var mem={},i,j,max=0;
    
    function findsquares(i,j){
        var k= i.toString(2)+":"+j.toString(2);											//To store a pair as key, we convert them to string
        if(k in mem)
            return mem[k];
        if(i==matrix.length-1 || j==matrix[0].length-1 || matrix[i][j]=='0'){
            mem[k]=parseInt(matrix[i][j]);
            return mem[k];
        }
        
        mem[k]=1+Math.min(findsquares(i+1,j),findsquares(i,j+1),findsquares(i+1,j+1));	//The length of a square which can be made using the current box as top-left
        																				//+1 is for the current box
    	return mem[k];
    }
    
    for(i=0;i<matrix.length;i++){
        for(j=0;j<matrix[0].length;j++){
            var n=findsquares(i,j);														//Max square length for each position is found and the max is stored
            max=Math.max(max,n);
        }
    }
    
    return max*max;																		
};
