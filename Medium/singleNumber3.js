/*
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only 
once. You can return the answer in any order.
You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Example 1:
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:
Input: nums = [-1,0]
Output: [-1,0]

Example 3:
Input: nums = [0,1]
Output: [1,0]
*/





/*
Logic: We XOR all the elements in the array, so that we are left with a^b where a and b occur once. Their answer's leftmost 1's position is noted by j. Now, we 
again iterate over the nums array and find which numbers have 1 at that position. We will XOR these elements so that duplicates are cancelled out. We will find
either a or b as xor2. Say if we find a, we can XOR it with a^b to find b. Then we push them into a list and return the list.
*/
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var singleNumber = function(nums) {
    var xor=0,i,x1;
    for(i=0;i<nums.length;i++)
        xor=nums[i]^xor;
    
    var j=1,l=[];
    while(true){
        if(j==(j&xor))
            break;
        j=j<<1;
    }
    
    var xor2=0;
    for(i=0;i<nums.length;i++){
        if((j&nums[i])==j)
            xor2=nums[i]^xor2;
    }
    
    l.push(xor2);
    l.push(xor^xor2);
    return l;
};
