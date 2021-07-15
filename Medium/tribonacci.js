/*
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537
*/




/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function(n) {
    if(n==0)						//1st no. is 0
        return 0;
    if(n==1 || n==2)				//2nd and 3rd no. is 1
        return 1;
    
    var a=0,b=1,c=1;
    var r=a+b+c;
    var i=3;						//Keeps track of the i-th Tribonacci

    while(i<n){
        a=b;
        b=c;
        c=r;
        r=a+b+c;
        i+=1;
    }
    
    return r;
};
