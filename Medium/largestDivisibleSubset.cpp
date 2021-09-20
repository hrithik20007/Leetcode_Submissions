/*
Given a set of distinct positive integers nums, return the largest subset answer such that every pair 
(answer[i], answer[j]) of elements in this subset satisfies:
    answer[i] % answer[j] == 0, or
    answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

Example 1:
Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

Example 2:
Input: nums = [1,2,4,8]
Output: [1,2,4,8]
*/






/*
Logic: Watch Tech Dose Video for full explaination. Dp array holds the maximum size of a subset uptil that length.
From dp array, we then proceed to find the actual subset.
*/
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n=nums.size();
        vector<int> dp(n+1,1);
        
        int i,prev=-1,maximum=1;
        for(i=1;i<n;++i){
            
            for(int j=0;j<i;++j){
                if(nums[i]%nums[j]==0 && dp[j]+1>dp[i]){
                    dp[i]=1+dp[j];
                    if(maximum<dp[i])
                        maximum=dp[i];
                }
            }
        }
        
        vector<int> res;
        for(i=n-1;i>=0;i--){
            if(dp[i]==maximum && (prev%nums[i]==0 || prev==-1)){
                res.push_back(nums[i]);
                maximum-=1;
                prev=nums[i];
            }
        }
        
        return res;






    /*
    Time Limit Exceeds


        vector<int> helper(int idx, int len, vector<int> l, vector<int> nums){
            if(idx==nums.size())
                return l;
            
            vector<int> a,b;
            a=helper(idx+1,len,l,nums);
            if((len>0 && (nums[idx]%(l.back()))==0) || len==0){
                l.push_back(nums[idx]);
                b=helper(idx+1,len+1,l,nums);
                l.pop_back();
            }
            
            if(a.size()>b.size())
                return a;
            else
                return b;
        }
        
        vector<int> largestDivisibleSubset(vector<int>& nums) {
            vector<int> l;
            sort(nums.begin(),nums.end());
            
            return helper(0,0,l,nums);
            
    */
    }
};