/*
Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.
A boomerang is a set of three points that are all distinct and not in a straight line.

Example 1:
Input: points = [[1,1],[2,3],[3,2]]
Output: true

Example 2:
Input: points = [[1,1],[2,2],[3,3]]
Output: false
*/





/**
 * @param {number[][]} points
 * @return {boolean}
 */
var isBoomerang = function(points) {
    var f=0;
    if(points[0][0]==points[1][0] && points[0][1]==points[1][1])
        f+=1;
    if(points[1][0]==points[2][0] && points[1][1]==points[2][1])
        f+=1;
    if(points[0][0]==points[2][0] && points[0][1]==points[2][1])		//Checking if the points are distinct
        f+=1;
    if(points[0][0]==points[1][0] && points[1][0]==points[2][0])
        f+=1;
    if(points[0][1]==points[1][1] && points[1][1]==points[2][1])		//Checking if all the points are in same x-axis or y-axis. If yes, then they are in single line
        f+=1;
    
    if(f!=0)
        return false;
    
    var l,r;
    l=(points[1][1]-points[0][1])/(points[1][0]-points[0][0]);			//Slope of 1st two points
    r=(points[2][1]-points[1][1])/(points[2][0]-points[1][0]);			//Slope of 2nd two points
    
    if(l!=r)															//If the slopes are equal, then they are collinear (not boomerang)
        return true;
    else
        return false;
};
