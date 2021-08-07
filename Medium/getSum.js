/*
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3

Example 2:

Input: a = 2, b = 3
Output: 5

*/




/*Logic: We are calculating the sum as xor, but without adding the carry from the previous bit, if both were 1. We do so, in the next iteration via recursion.
Take note that we have given carry<<1 as parameter because the carry 1 is always added to the bits at just the left of its position.
*/
/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function(a, b) {
    var xor=a^b;
    var carry=a&b;
    
    if(carry==0) return xor;
    return getSum(xor,carry<<1);
};
