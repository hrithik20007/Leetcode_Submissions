/*
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or 
index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10
*/



/*
Solved using recursion. 
The elements are added on their way up, so as to use memoization. Because when adding on their way up from the bottom, each point in a particular row will give 
the unique value. However, if we add on our way down, then the addition returned on their way up will differ even for same point in a particular row. It is because
the path taken on the way down to reach a particular point is not predictable, yielding different addition values for same point. We cannot do memoization that 
way. However, while adding on their way up, each point will always give a specific value. We can thus perform memoization.  
*/
/**
 * @param {number[][]} triangle
 * @return {number}
 */
function steps(triangle,idx,r,mem){
    if(r==triangle.length-1)
        return triangle[r][idx];
    if(r+':'+idx in mem)
        return mem[r+':'+idx];
    
    mem[r+':'+idx]=Math.min(steps(triangle,idx,r+1,mem),steps(triangle,idx+1,r+1,mem)) + triangle[r][idx];	//Adds the current value to the minimum of the returned values
    
    return mem[r+':'+idx];
}

var minimumTotal = function(triangle) {
    return steps(triangle,0,0,{});
};
