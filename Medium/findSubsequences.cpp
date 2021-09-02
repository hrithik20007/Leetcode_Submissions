/*
Given an integer array nums, return all the different possible increasing subsequences of the given array with at least two elements. You may return the answer in 
any order.
The given array may contain duplicates, and two equal integers should also be considered a special case of increasing sequence.

Example 1:
Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

Example 2:
Input: nums = [4,4,3,2,1]
Output: [[4,4]]
*/







/*
Logic: We are either adding an index element or ignoring it. While adding we make sure that the new element to be added is >= the last element which was added.
These elements are added to a vector, which in turn is added to a 'set'(of vectors). The set makes sure that the same vector is not added twice. 
*/
class Solution {
public:
    void helper(int idx, vector<int> &nums, vector<int> s, set<vector<int>> &ans){
        if(idx==nums.size()){
            if(s.size()>1)
                ans.insert(s);										//Adding elements to the set (only unique ones get added)
            return;
        }
        
        if(s.size()>=1 && nums[idx]>=s.back()){						//s.back() is the same as s[s.size()-1] and gives the last element of s
            s.push_back(nums[idx]);
            helper(idx+1,nums,s,ans);
            s.pop_back();
            helper(idx+1,nums,s,ans);
        }
        else if(s.size()==0){
            s.push_back(nums[idx]);
            helper(idx+1,nums,s,ans);
            s.pop_back();
            helper(idx+1,nums,s,ans);
        }
        else
            helper(idx+1,nums,s,ans);
        
    }
    
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        vector<int> s;
        set<vector<int>> ans;
        
        helper(0,nums,s,ans);
        return vector<vector<int>> (ans.begin(),ans.end());			//Printing the set as a vector of vectors
    }
};
