/*
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the 
XY plane.

Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
*/





/**
 * @param {number[][]} coordinates
 * @return {boolean}
 */
var checkStraightLine = function(coordinates) {
    var s,slope,f=0;
    if(coordinates[1][0]==coordinates[0][0]){			//In this case, slope becomes infinity and they'll have the same x-coordinates
        f=1;
        var x=coordinates[1][0];
    }

    slope=(coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0]);
    
    for(i=2;i<coordinates.length;i++){
        if(f==1){										//For infinite slope
            if(coordinates[i][0]==x)
                continue;
            else
                return false;
        }
        
        s=(coordinates[i][1]-coordinates[i-1][1])/(coordinates[i][0]-coordinates[i-1][0]);		//If slope is not infinite, then we check if the slope is same for
        																						//all the points
        if(s!=slope)
            return false;
    }
    
    return true;
};
