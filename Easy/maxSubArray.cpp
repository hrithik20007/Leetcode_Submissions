/*
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its 
sum.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
*/






/*
Logic: Using Kadane's Algorithm. We take ans as the minimum integer. s holds the sum till the current element of the vector. However,
if the sum becomes -ve, that means that from the initial position till that position the sum becomes -ve and thus ideally we start
a new subarray sum from that posiiton. ans holds the maximum sum possible.
*/
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int i,s=0,ans=INT_MIN;
        
        for(i=0;i<nums.size();i++){
            s+=nums[i];
            ans=max(ans,s);
            if(s<0)
                s=0;
        }
        
        return ans;
    }
};