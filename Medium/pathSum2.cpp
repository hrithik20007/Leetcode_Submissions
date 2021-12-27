/*
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values 
in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []
*/






/*
Logic: Solved recursively using backtracking. All the combinations are put into a temporary vector and only the values 
which add up to targetSum and are put into the final vector 'ans'.
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
    vector<vector<int>> ans;
    
    void helper(TreeNode *root, int targetSum, int s, vector<int> l){
        if(!(root->left) && !(root->right)){
            s+=root->val;
            l.push_back(root->val);
            if(s==targetSum)
                ans.push_back(l);
            return;
        }
        
        l.push_back(root->val);
        if(root->left)
            helper(root->left,targetSum,s+root->val,l);
        if(root->right)
            helper(root->right,targetSum,s+root->val,l);
        return;
    }
    
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<int> l;
        int s=0;
        if(root==NULL)
            return ans;
        
        helper(root,targetSum,s,l);
        return ans;
    }
};