/*
There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform 
some increment operations on the matrix.
For each location indices[i], do both of the following:
    Increment all the cells on row ri.
    Increment all the cells on column ci.
Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.

Example 1:
Input: m = 2, n = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.

Example 2:
Input: m = 2, n = 2, indices = [[1,1],[0,0]]
Output: 0
Explanation: Final matrix = [[2,2],[2,2]]. There are no odd numbers in the final matrix.
*/




/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} indices
 * @return {number}
 */
var oddCells = function(m, n, indices) {
    var i,j,x,y,j1,j2,l=[],grid=[],c=0;
    for(i=0;i<m;i++){
        l=[];
        for(j=0;j<n;j++){
            l.push(0);
        }
        grid.push(l);
    }

    for(i of indices){
        x=i[0];
        y=i[1];
        
        for(j1=0;j1<m;j1++)
            grid[j1][y]+=1;
        for(j2=0;j2<n;j2++)
            grid[x][j2]+=1;
    }

    for(i=0;i<m;i++){
        for(j=0;j<n;j++){
            if(grid[i][j]%2!=0)
                c+=1;
        }
    }
    
    return c;
};
