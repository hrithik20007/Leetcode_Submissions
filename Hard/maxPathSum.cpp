/*
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting 
them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
*/






/*
Logic: We solve this using a bottom-up recursive approach. We calculate the maximum path value uptil any node by having the
maximum of the current node, the current + left subtree, the current + right subtree and finally, the current + left 
subtree + right subtree. This is stored by a global variable. However, when we return the max uptil the node below to the
adjacent upper node, we omit the curr+left+right value as that itself is a path. When we go to the upper node, it becomes
a different path.
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
    int ans=INT_MIN;
    
    int helper(TreeNode* root){
        if(root==NULL)
            return 0;
        
        int curr=root->val;
        int left=helper(root->left);
        int right=helper(root->right);
        int maximum=max(max(left+right+curr,curr),max(curr+left,curr+right));
        ans=max(maximum,ans);
        
        return max(curr,max(left+curr,right+curr));
    }
    
    int maxPathSum(TreeNode* root) {
        helper(root);
        return ans;
    }
};