/*
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Example 1:
Input: left = 5, right = 7
Output: 4

Example 2:
Input: left = 0, right = 0
Output: 0

Example 3:
Input: left = 1, right = 2147483647
Output: 0
*/





/**
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var rangeBitwiseAnd = function(left, right) {
    if(left==0)
        return 0;
    
    var i,j;
    for(i=1;i<=31;i++){
        j=Math.pow(2,i);
        if(left<j && j<=right)			//If there is a power of 2 between left and right (including the right), AND will always give 0.
            return 0;					//For example, 3=11 and 4=100. Thus 3 & 4 will be 0. Also, 0 & x always gives 0 (whatever x maybe). 
    }
    
    var s=left;							//If we reach here, it means there was no 0 or multiple of two after left until right. So the answer cannot be 0.
    for(i=left+1;i<=right;i++){
        s=s&i;
    }
    return s;
};
