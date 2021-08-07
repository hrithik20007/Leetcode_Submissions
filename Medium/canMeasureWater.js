/*
You are given two jugs with capacities jug1Capacity and jug2Capacity liters. There is an infinite amount of water supply available. Determine whether it is possible 
to measure exactly targetCapacity liters using these two jugs.
If targetCapacity liters of water are measurable, you must have targetCapacity liters of water contained within one or both buckets by the end.
Operations allowed:
    Fill any of the jugs with water.
    Empty any of the jugs.
    Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.

Example 1:
Input: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
Output: true
Explanation: The famous Die Hard example 

Example 2:
Input: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
Output: false

Example 3:
Input: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
Output: true
*/




/*
Logic: We can convert the problem into the equation ax+by=d, when x and y are jug1 and jug2, while a and b are integers. According to Bezout's theorem, a and b exist
when d is the multiple of GCD of x and y. a and b basically represent the number of times the jugs were emptied or filled. -ve a or b would indicate emptying, while
+ve would indicate getting filled. 
*/
/**
 * @param {number} x
 * @param {number} y
 * @param {number} z
 * @return {boolean}
 */
var canMeasureWater = function(x, y, z) {
    if(x+y<z)
        return false;
    
    var a,b,r;
    if(x<=y){
        a=x;
        b=y;
    }
    else{
        a=y;
        b=x;
    }
    
    r=b%a;
    while(r!=0){
        b=a;
        a=r;
        r=b%a;
    }						//Uptil this point, we have found the GCD of x and y, which is a
  	  
    return (z%a==0)			//If the target is a multiple of the GCD, then we return true
};
