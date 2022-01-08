/*
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two 
different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1
*/







/*
Logic:
First we get a sorted vector of all the node values (by inorder traversal). Then we find the difference of every 
consecutive elements. We finally return the minimum difference.
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
    void inorder(TreeNode *root,vector<int> &v){
        if(root==NULL) return;
        inorder(root->left,v);
        v.push_back(root->val);
        inorder(root->right,v);
    }
    
    int getMinimumDifference(TreeNode* root) {
        vector<int> v;
        inorder(root,v);
    
        int m=INT_MAX;    
        for(int i=0;i<v.size()-1;i++){
            int d=v[i+1]-v[i];
            m=abs(min(m,d));
        }
        
        return m;
    }
};