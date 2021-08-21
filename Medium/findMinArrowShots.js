/*
There are some spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. 
Since it's horizontal, y-coordinates don't matter, and hence the x-coordinates of start and end of the diameter suffice. The start is always smaller than the end.
An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. 
There is no limit to the number of arrows that can be shot. An arrow once shot keeps traveling up infinitely.
Given an array points where points[i] = [xstart, xend], return the minimum number of arrows that must be shot to burst all balloons.

Example 1:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).

Example 2:
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4

Example 3:
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
*/





/*
Logic: We sort the points by their ending limit. We increase the arrow count only when the starting limit of the next points exceeds the ending limit uptil that point.
*/
/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function(points) {
    var i,c=0,end=Number.MIN_SAFE_INTEGER;
    
    points.sort((a,b)=>a[1]-b[1]);
    
    for(i=0;i<points.length;i++){
        if(points[i][0]>end){
            end=points[i][1];
            c+=1;
        }
    }
    
    return c;
};





/*
var findMinArrowShots = function(points) {
    
    var i,j,dict={},l=[];
    for(i=0;i<points.length-1;i++){
        if(l.includes(i))
            continue;
        
        for(j=i+1;j<points.length;j++){
            if(i==j)
                continue;
            
            var a=points[i][0];
            var b=points[i][1];
            var c=points[j][0];
            var d=points[j][1];
            if((c<=a && a<=d) || (c<=b && b<=d) || (a<=c && c<=b) || (a<=d && d<=b)){
                //console.log(dict);
                if(points[i] in dict)
                    dict[points[i]]+=1;
                else
                    dict[points[i]]=2;
                
                l.push(j);
                //console.log("L : ",l);
            }
        }
        
        if(!(points[i] in dict))
            dict[points[i]]=1;
    }
    
    if(!(points[i] in dict) && !(l.includes(i)))
        dict[points[i]]=1;
    
    
    var keys=Object.keys(dict);
    console.log(dict);
    return keys.length;  
};
*/
