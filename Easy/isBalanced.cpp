/*
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
*/





/*
Logic: Recursively, we first go to the bottom-most nodes. From there, we check whether the left and right sub-tree height
is less than or equal to 1. If yes, then we return the maximum height from the two subtrees for checking balanced condition
for the upper nodes. If no, then we simply return -1. Also, if we encounter a -1 at any point, we will keep returning -1
as the condition failing at one point means the total balanced conditon has failed.
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
    int helper(TreeNode *root){
        if(root==NULL)
            return 0;
        
        int d1=helper(root->right);
        int d2=helper(root->left);
        
        if(d1==-1 || d2==-1 || abs(d1-d2)>1)
            return -1;
        else
            return max(d1,d2)+1;
    }
    
    bool isBalanced(TreeNode* root) {
        int f=helper(root);
        if(f==-1)
            return false;
        else
            return true;
    }
};