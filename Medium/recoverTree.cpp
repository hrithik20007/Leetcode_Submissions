/*
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Example 1:
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example 2:
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
*/







/*
Logic:
We traverse the BST in inorder path, meaning in sorted order. If we encounter a smaller value than before, we mark the
smaller value as 'mid' and the larger previous no. as 'first'. If we encounter a similar scenario again, we mark the 
smaller value as 'last'. If no such scenario arises, the 'last' pointer remains NULL. 
The first case is when the swapped values are away from each other.
The second case is when the swapped values are consecutive.
If first and last exists, we swap them; otherwise we swap first and mid.
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
    void helper(TreeNode *root, TreeNode* &prev,TreeNode* &first,TreeNode* &mid,TreeNode* &last){
        if(root==NULL)
            return;
        
        helper(root->left,prev,first,mid,last);
        
        if(prev && prev->val>root->val){
            if(first==NULL){
                first=prev;
                mid=root;
            }
            else
                last=root;
        }
        
        prev=root;
        helper(root->right,prev,first,mid,last);
        
        return;
    }
    
    void recoverTree(TreeNode* root) {
        TreeNode *prev=NULL;
        TreeNode *first=NULL;
        TreeNode *mid=NULL;
        TreeNode *last=NULL;
        
        helper(root,prev,first,mid,last);
        
        int t;
        if(first && last){
            t=first->val;
            first->val=last->val;
            last->val=t;
        }
        else if(first && mid){
            t=first->val;
            first->val=mid->val;
            mid->val=t;
        }
        
        return;
    }
};