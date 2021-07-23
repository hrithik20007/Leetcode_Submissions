/*
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a 
circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact 
the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [0]
Output: 0
*/




/*
Logic: Similar to houseRobber, but since this one is a circle, we cannot have the first and last elements together in the sum as they are consecutive. We can have 
only one of them. So, we find the sums for two arrays -
1)nums without the 1st element
2)nums without the last element
Then we return the greater sum of the two.
*/ 
/**
 * @param {number[]} nums
 * @return {number}
 */
function robber(num){
    var a=0,b=0,t;
    for(i of num){
        t=Math.max(i+a,b);
        a=b;
        b=t;
    }
    return b;
}

var rob = function(nums) {
    var t=nums[0];
    nums.splice(0,1);
    var a=robber(nums);
    
    nums.pop();
    nums.unshift(t);
    var b=robber(nums);
    
    return Math.max(a,b);
};




/*
var rob = function(nums) {
    if(nums.length==1)
        return nums[0];
    if(nums.length==2)
        return Math.max(nums[0],nums[1]);
    
    var r=[],l=[0],p=0,ans=Math.max(nums[0],nums[1]);

    for(i=2;i<nums.length;i++){
        var max=-1;
        if(i!=nums.length-1){
            for(j=i-2;j>=0;j--){
                if(nums[j]>max){
                    max=nums[j];
                    if(j==p)
                        p=i;
                }
            }
        }
        else
            for(j=i-2;j>=1;j--){
                if(l.includes(j))
                    continue;
                if(nums[j]>max)
                    max=nums[j];				
            }
        l.push(p);
        nums[i]=nums[i]+max;
        ans=Math.max(ans,nums[i]);
    }
    
    return ans;
};
*/
