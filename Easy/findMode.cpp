/*
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred 
element) in it. If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [1,null,2,2]
Output: [2]

Example 2:
Input: root = [0]
Output: [0]
*/






/*
Logic:
At first we put all the node values in a map. After that, we go through the map via an iterator and find out the maximum 
frequency of the node values. Then we iterate over it again, this time pushing the node values with the highest frequency
into a vector 'ans'.
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
    map<int,int> m;
    vector<int> ans;
    
    void helper(TreeNode *root){
        if(root==NULL)
            return;
        
        m[root->val]+=1;
        
        helper(root->left);
        helper(root->right);
        
        return;
    }
    
    vector<int> findMode(TreeNode* root) {
        helper(root);
        
        int s=INT_MIN;
        for(auto it:m){
            if(s<it.second)
                s=it.second;
        }
        for(auto it1:m){
            if(it1.second==s)
                ans.push_back(it1.first);
        }
        
        return ans;
    }
};