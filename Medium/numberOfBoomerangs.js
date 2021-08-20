/*
You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and 
j equals the distance between i and k (the order of the tuple matters).
Return the number of boomerangs.

Example 1:
Input: points = [[0,0],[1,0],[2,0]]
Output: 2
Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].

Example 2:
Input: points = [[1,1],[2,2],[3,3]]
Output: 2

Example 3:
Input: points = [[1,1]]
Output: 0
*/





/**
 * @param {number[][]} points
 * @return {number}
 */
var numberOfBoomerangs = function(points) {
    if(points.length<3)
        return 0;
    
    var i,j,dist,c=0;
    for(i=0;i<points.length;i++){
        var d={};
        for(j=0;j<points.length;j++){
            if(i==j)
                continue;

            dist=Math.pow(points[i][0]-points[j][0],2)+Math.pow(points[i][1]-points[j][1],2);

            if(dist in d)
                d[dist]+=1;
            else
                d[dist]=1;
            
            if(d[dist]>1)
                c+=(d[dist]-1)*2;
        }
    }
    
    return c;
};
