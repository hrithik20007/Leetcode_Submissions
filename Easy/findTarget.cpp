/*
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that 
their sum is equal to the given target.

Example 1:
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
*/






/*
Logic:
By inorder traversal, we are able to push node values into a vector in sorted order (ony in cases of BST). Then we can
find whether we have two elements which sum up to the target, by traversing the vector by two-pointer method.
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
    
    bool findTarget(TreeNode* root, int k) {
        vector<int> v;
        inorder(root,v);
        
        int s=0,e=v.size()-1;
        while(s<e){
            int t=v[s]+v[e];
            if(t==k)
                return true;
            else if(t<k)
                s+=1;
            else
                e-=1;
        }
        
        return false;
    }
};