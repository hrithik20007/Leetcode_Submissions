/*
A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring stops where distance[i] is the distance between 
the stops number i and (i + 1) % n.
The bus goes along both directions i.e. clockwise and counterclockwise.
Return the shortest distance between the given start and destination stops.

Example 1:
Input: distance = [1,2,3,4], start = 0, destination = 1
Output: 1
Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.

Example 2:
Input: distance = [1,2,3,4], start = 0, destination = 2
Output: 3
Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.

Example 3:
Input: distance = [1,2,3,4], start = 0, destination = 3
Output: 4
Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.
*/






/**
 * @param {number[]} distance
 * @param {number} start
 * @param {number} destination
 * @return {number}
 */
var distanceBetweenBusStops = function(distance, start, destination) {
    var i=start+1,s1=distance[start];
    while(i!=destination){              //clock-wise
        if(i==distance.length)
            i=0;
        if(i==destination)				//To check after changing i to 0. This is not checked in the while loop as i is increamented before that. 
            break;
        s1+=distance[i];
        i+=1;
    }
    
    var j=start-1,s2=0;
    while(j!=destination-1){            //anti-clockwise
        if(j==-1)
            j=distance.length-1;
        if(j==destination-1)			//To check after changing j to distance.length-1. This is not checked in the while loop as j is decreamented before that. 
            break;
        s2+=distance[j];
        j-=1;
    }
    
    if(s1<s2)
        return s1;
    else
        return s2;
};
