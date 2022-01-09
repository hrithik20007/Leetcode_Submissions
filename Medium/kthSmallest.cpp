/*
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of 
the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
*/







/*
Logic:
By inorder traversal, we get a sorted vector. Then we just return the (k-1)th indexed element.
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
    vector<int> in;
    void inorder(TreeNode *root){
        if(root==NULL)
            return;
        
        inorder(root->left);
        in.push_back(root->val);
        inorder(root->right);
        return;
    }
    
    int kthSmallest(TreeNode* root, int k) {
        inorder(root);
        
        return in[k-1];
    }
};