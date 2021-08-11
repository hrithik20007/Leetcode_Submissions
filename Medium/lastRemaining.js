/*
You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order. Apply the following algorithm on arr:
    Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
    Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
    Keep repeating the steps again, alternating left to right and right to left, until a single number remains.
Given the integer n, return the last number that remains in arr.

Example 1:
Input: n = 9
Output: 6
Explanation:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [2, 4, 6, 8]
arr = [2, 6]
arr = [6]

Example 2:
Input: n = 1
Output: 1
*/





/*
Logic: We are updating our starting value with each iteration. From the example, we see when we start elimination from the left, starting element always gets
eliminated. Also if the number of elements in the array is odd, then also the starting elements gets eliminated irrespective of the direction of elimination.
step keeps track of the increament value after each elimination. Before 1st elimination, the values increase by 1. After that, the values increase by 2. That's step.
So, when we do have to change our starting, we increase it by the step.
*/
/**
 * @param {number} n
 * @return {number}
 */
var lastRemaining = function(n) {
    var start=1,remaining=n,step=1,left=true;		//remaining means the number of elements in the array; left means the direction of elimination is left
    
    while(remaining>1){
        if(left===true || remaining%2==1)
            start+=step;
        
        remaining=Math.trunc(remaining/2);			//remaining decreases to 1/2 of its previous value
        step*=2;									//step multiplies by 2
        left=!left;									//direction of elimination alternates
    }
    
    return start;
};







/*
var lastRemaining = function(n) {
    
    var l=[],i,idx;
    for(i=0;i<n;i++){
        l.push(i+1);
    }
    console.log(l);
    while(l.length>1){
        //console.log(1,l);  
        idx=0;
        while(idx<=l.length-1){
            l.splice(idx,1);
            idx+=1;
        }
        
        if(l.length==1)
            break;
        
        idx=l.length-1;
        while(idx>=0){
            l.splice(idx,1);
            idx-=2;         
        }
        //console.log(3,l);
    }
    //console.log(l);
    return l[0];
};
*/
