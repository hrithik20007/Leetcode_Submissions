/*
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
The answer is guaranteed to fit in a 32-bit integer.

Example 1:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

Example 2:
Input: nums = [9], target = 3
Output: 0
*/





/*
Logic: We solve this using recursion. We use a for loop and deduct nums[i] from target at each step. If we reach target, we return 1. If it is more or exceeds the 
target, we return 0. We also use memoization of the target at a particular step. If the target is reached again in any other step, we already know what we will
eventually get. 
*/
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var combinationSum4 = function(nums, target) {
    nums.sort((a,b)=>a-b);
    var mem={};
    
    function combination(target){
        if(target in mem)
            return mem[target];
        if(target==0)
            return 1;
        if(target<0)
            return 0;
        
        var c=0;
        for(var i=0;i<nums.length;i++){
            if(nums[i]>target)
                break;
            c+=combination(target-nums[i]);
        }
        
        mem[target]=c;
        return mem[target];
    }
    
    return combination(target);
};
