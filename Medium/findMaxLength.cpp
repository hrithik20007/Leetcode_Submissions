/*
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
*/






/*
Logic: We change all the 0s in the vector to -1. Thus, we have to find the largest subarray which adds to 0. We keep adding the bits in nums (1 for 1 and -1 for 0).
If we have sums (say 2) at any two points, that means that the total sum of elements after that position till now has summed to 0. That means from the previous s=2
position till the current s=2 position, there is a subarray whose sum is 0. We consider its length and the maximum such length will be our answer. Also note that if
at any point our s=0, then we take the subarray length from the starting position of the vector.
We keep track of the previous s=2(as said) position using a Hashmap. 
*/
class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int,int> mem;
        int i,s=0,ans=0;

        for(i=0;i<nums.size();i++){
            s+=(nums[i]==0)?-1:1;
            if(s!=0 && mem.count(s)==1)
                ans=max(i-mem[s],ans);
            else
                mem[s]=i;
            
            if(s==0)
                ans=max(i+1,ans);
        }
        
        return ans;
    }
};






/*
class Solution {
public:
    int helper(vector<int>& nums, int idx, int zero, int one, int l){
        if(idx==nums.size() && one==zero)
            return l;
        if(idx==nums.size() && one!=zero)
            return 0;
        
        int a=0,b=0;
        if(nums[idx]==0)
            a=helper(nums,idx+1,zero+1,one,l+1);
        else
            a=helper(nums,idx+1,zero,one+1,l+1);
        b=helper(nums,idx+1,zero,one,l);
        cout<<a<<" "<<b<<endl;
        return max(a,b);
    }
    
    int findMaxLength(vector<int>& nums) {
        return helper(nums, 0, 0, 0, 0);
    }
};
*/
