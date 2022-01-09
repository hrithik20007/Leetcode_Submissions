/*
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
*/






/*
Logic:
Solved using top-down recursion approach. If at any point, the conditions are not satisfied, we return false. If we reach 
NULL, we return true. For left sub-tree, the root values can have a maximum value less than the current root value, while
for right sub-tree, the root values can have a minimum value more than the current root value.
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
    bool helper(TreeNode *root,TreeNode *min,TreeNode *max){
        if(root==NULL)
            return true;
        if(min!=NULL && root->val<=min->val)
            return false;
        if(max!=NULL && root->val>=max->val)
            return false;
        
        bool left=helper(root->left,min,root);
        bool right=helper(root->right,root,max);
        
        return left && right;
    }
    
    bool isValidBST(TreeNode* root) {
        return helper(root,NULL,NULL);
    }
};