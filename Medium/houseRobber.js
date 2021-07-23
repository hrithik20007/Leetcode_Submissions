/*
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing 
each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the 
same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
*/




/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    var a=0,b=0,t;				//a stores the second maximum no. and b stores the maximum no. uptil any position of the nums array (without adding two consecutive
    							//numbers)
    for(i of nums){
        t=Math.max(i+a,b);
        a=b;
        b=t;
    }
    return b;
};



/*
//Works but utilises O(n) space.

var rob = function(nums) {
    if(nums.length==1)
        return nums[0];
    if(nums.length==2)
        return Math.max(nums[0],nums[1]);
    
    var r=[],max=[],t,j,i;
    if(nums[0]>=nums[1]){
        j=0;
        max=[nums[1],nums[0]];
    }
    else{
        j=1;
        max=[nums[0],nums[1]];
    }
    
    for(i=2;i<nums.length;i++){
        if(j==i-1)
            nums[i]+=max[max.length-2];
        if(j!=i-1)
            nums[i]+=max[max.length-1];

        if(nums[i]>max[max.length-2] && nums[i]<max[max.length-1]){
            t=max[max.length-1];
            max.pop();
            max.push(nums[i]);
            max.push(t);
        }
        else if(nums[i]>=max[max.length-1]){
            j=i;
            max.push(nums[i]);
        }
    }
    
    return max[max.length-1];
};
*/





/*
Logic: Every position would contain the optimal sum (i.e. the max sum possible upto that element), but we must ignore the previous element (as consecutive robbing
is not allowed).  
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if(nums.length==1)
        return nums[0];
    if(nums.length==2)
        return Math.max(nums[0],nums[1]);
    
    var r=[];

    for(i=2;i<nums.length;i++){
        var max=-1;								//max must be re-initialized at every iteration
        for(j=i-2;j>=0;j--){
            if(nums[j]>max)
                max=nums[j];					//max contains the maximum sum/element until the given position, which is i (we ignore the element at i-1)
        }
        nums[i]=nums[i]+max;
    }
    
    return Math.max(nums[nums.length-1],nums[nums.length-2]);
};
