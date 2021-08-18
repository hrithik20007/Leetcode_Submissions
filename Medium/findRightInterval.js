/*
You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.
The right interval for an interval i is an interval j such that startj >= endi and startj is minimized.
Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.

Example 1:
Input: intervals = [[1,2]]
Output: [-1]
Explanation: There is only one interval in the collection, so it outputs -1.

Example 2:
Input: intervals = [[3,4],[2,3],[1,2]]
Output: [-1,0,1]
Explanation: There is no right interval for [3,4].
The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.

Example 3:
Input: intervals = [[1,4],[2,3],[3,4]]
Output: [-1,2,-1]
Explanation: There is no right interval for [1,4] and [3,4].
The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.
*/





/*
Logic: We store the original indexes of the intervals in a dictionary (first element being the key) and then sort it by the first element. After sorting, we are sure 
that the element >= to the second element of any interval will be after it. We use j to find the required right interval and use the dictionary to input that in the
list l by their original indexes.
*/
/**
 * @param {number[][]} intervals
 * @return {number[]}
 */
var findRightInterval = function(intervals) {
    var i,j,d={},l=[];
    for(i=0;i<intervals.length;i++){
        d[intervals[i][0]]=i;
        l.push(0);
    }
    
    intervals.sort((a,b)=>a[0]-b[0]);
    
    for(i=0;i<intervals.length;i++){
        j=i;
        while(j<intervals.length && intervals[i][1]>intervals[j][0])
            j+=1;

        if(j>=intervals.length)
            l[d[intervals[i][0]]]=-1;
        else
            l[d[intervals[i][0]]]=d[intervals[j][0]];
    }
    
    return l;
};
