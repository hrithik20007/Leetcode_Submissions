/*
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf 
node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Example 3:
Input: root = []
Output: 0

Example 4:
Input: root = [0]
Output: 1
*/




/*
Logic: We solve this using recursion. When we encounter a NULL and return to its parent node, the length becomes 1 for
that parent node (as we include a +1 in the previous call, i.e. 0(for left subtree)+0(for right subtree)+1(for current 
node)).Consequently, we take the maximum length between the subtree heights and by the time we reach back the root, we 
have the height(or depth) of the tree. 
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
    int maxDepth(TreeNode* root) {
        if(root==NULL)
            return 0;
        
        return max(maxDepth(root->left),maxDepth(root->right))+1;
    }
};