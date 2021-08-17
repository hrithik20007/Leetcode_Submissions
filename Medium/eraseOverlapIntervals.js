/*
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the 
intervals non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
*/







/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function(intervals) {
    intervals.sort((a,b)=>a[1]-b[1]);					//We sort the intervals by their second element
    var i,end=Number.MIN_SAFE_INTEGER,c=0;
    
    for(i=0;i<intervals.length;i++){
        if(intervals[i][0]>=end)
            end=intervals[i][1];						//We update end by their second element when the first element is greater than or equal to it
        else
            c+=1;										//Otherwise we increase c, which stores the number of overlapping intervals
    }
    
    return c;
};
