/*
We are given a matrix with rows rows and cols columns has cells with integer coordinates (r, c), where 0 <= r < rows and 0 <= c < cols.
Additionally, we are given a cell in that matrix with coordinates (rCenter, cCenter).
Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter) from smallest distance to largest distance.  Here, the distance 
between two cells (r1, c1) and (r2, c2) is the Manhattan distance, |r1 - r2| + |c1 - c2|.  (You may return the answer in any order that satisfies this condition.)

Example 1:
Input: rows = 1, cols = 2, rCenter = 0, cCenter = 0
Output: [[0,0],[0,1]]
Explanation: The distances from (0, 0) to other cells are: [0,1]

Example 2:
Input: rows = 2, cols = 2, rCenter = 0, cCenter = 1
Output: [[0,1],[0,0],[1,1],[1,0]]
Explanation: The distances from (0, 1) to other cells are: [0,1,1,2]
The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.

Example 3:
Input: rows = 2, cols = 3, rCenter = 1, cCenter = 2
Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
Explanation: The distances from (1, 2) to other cells are: [0,1,1,2,2,3]
There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].
*/





/**
 * @param {number} rows
 * @param {number} cols
 * @param {number} rCenter
 * @param {number} cCenter
 * @return {number[][]}
 */
var allCellsDistOrder = function(rows, cols, rCenter, cCenter) {
    var i,j,dist;
    var arr=[];
    for(i=0;i<rows;i++){
        for(j=0;j<cols;j++){
            dist=Math.abs(i-rCenter)+Math.abs(j-cCenter);
            arr.push([i,j,dist]);								//A three-element list is added at every iteration, the third element being the distance 
        }
    }
    return arr.sort((a,b)=>a[2]-b[2]).map(a=>a.slice(0,-1))		//The lists are sorted as per their third element by the sort() parameter function defined. 
    															//slice() returns a portion of a list as per the given indices (excluding the last index). In case
    															//of negative indices, it is counted from the last. -1 will mean till the second last element.
    															//That means we cut the third element or the distance.
};




    /*
	This works with almost the same speed but the above solution is simpler


    
    var i,j;
    var arr=[],l=[],r=[];
    var d={};
    for(i=0;i<rows;i++){
        for(j=0;j<cols;j++){
            arr.push([i,j]);
        }
    }
    
    for(i of arr){
        var dist=Math.abs(rCenter-i[0])+Math.abs(cCenter-i[1]);
        if (dist in d)
            d[dist].push(i);
        else
            d[dist]=[i];
        l.push(dist);
    }
     
    l.sort((a,b)=>a-b);				//sort() uses different algorithms for sorting (Google,Safari uses QuickSort while Mozilla,Firefox uses MergeSort).
    								//Compares two elements, if -ve or 0, then dosen't change order, otherwise changes. This continues until there is no +ve 
    								//comparison results left.
    for(i of l){
        if(d[i].length==1)
            r.push(d[i][0]);
        else
            r.push(d[i].shift());
    }
    return r;
    */
