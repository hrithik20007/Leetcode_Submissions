/*
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99
*/




//We can also solve this using bit manipulation via checking all the 32 bits where the no. of bits is not a multiple of 3.
//Our solution is not really intuitive. Ones keeps track of the element which has occured only once until a particular iteration while twos keeps track of the 
//element which has occured twice. We do not keep track of the elements which have occured thrice. At last, we return ones because it is the element which has 
//occured once.
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    var ones=0;
    var twos=0;
    
    for(i of nums){
        ones=(ones^i) & ~(twos);		//^ indicates XOR while ~ indicates COMPLEMENT.
        twos=(twos^i) & ~(ones);
    }
    
    return ones;
};
