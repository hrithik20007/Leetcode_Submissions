/*
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary 
search tree.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more 
than one.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
*/






/*
Logic: 
The mid-point of the array will be the root. Values smaller than the root will be on the left sub-tree, while values
greater than it will be on the right sub-tree. We solve this recursively. Base cases are if the starting and ending point
become same, then we return the node with the value at that index. If starting index exceeds ending, then we return NULL.
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* sortBST(vector<int> nums,int start,int end){
        if(start==end){
            TreeNode *root=new TreeNode(nums[end]);
            return root;
        }
        if(start>end)
            return NULL;
        
        int idx=floor((end+start)/2);
        TreeNode *root=new TreeNode(nums[idx]);
        
        root->left=sortBST(nums,start,idx-1);
        root->right=sortBST(nums,idx+1,end);
        
        return root;
    }
    
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if(nums.size()<1)
            return NULL;
        
        return sortBST(nums,0,nums.size()-1);
    }
};