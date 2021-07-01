/*
You are given a binary array nums (0-indexed).
We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).
    For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
Return an array of booleans answer where answer[i] is true if xi is divisible by 5.

Example 1:
Input: nums = [0,1,1]
Output: [true,false,false]
Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.

Example 2:
Input: nums = [1,1,1]
Output: [false,false,false]

Example 3:
Input: nums = [0,1,1,1,1,1]
Output: [true,false,false,false,true,false]

Example 4:
Input: nums = [1,1,1,0,1]
Output: [false,false,false,false,false]
*/




/**
 * @param {number[]} nums
 * @return {boolean[]}
 */
var prefixesDivBy5 = function(nums) {
    var r=0;
    var l=[];
    l=nums.map((a)=>{
        r=r*2+a;			//If the bit (i.e. the array element) to be added is 0, then the updated number of the binary will be doubled otherwise doubled+1. 
        r=r%5;				//To prevent overflow (the remainder will be consistent even if the number itself becomes the remainder).
        					//For example, 7*2+1=15(remainder will be 0 when divided by 5). Also (7%5)*2+1=5(remainder will be 0 when divided by 5).
        return r==0;		//Returns true if remainder is 0, otherwise false
    });
    return l;
};




/*
    var i;
    var l=[];
    for(i=1;i<nums.length+1;i++){
        n=parseInt(nums.slice(0,i).join(''),2);
        if(n%5==0)
            l.push(true);
        else
            l.push(false);
    }
    return l
*/
