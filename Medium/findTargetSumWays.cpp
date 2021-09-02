/*
You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1
*/






/*
We either place a '+' or '-' before the the current index's element and add that to the total s. If by the end, the total matches the target, we increase ans by 1.
*/
class Solution {
public:
    void helper(int idx, int s, vector<int>& nums, int target, int &ans){
        if(idx==nums.size()){
            if(s==target)
                ans+=1;
            return;
        }
        
        helper(idx+1,s+nums[idx],nums,target,ans);
        helper(idx+1,s-nums[idx],nums,target,ans);
    }
    
    int findTargetSumWays(vector<int>& nums, int target) {
        int s=0;
        int ans=0;
        helper(0,s,nums,target, ans);
            
        return ans;
    }
};
