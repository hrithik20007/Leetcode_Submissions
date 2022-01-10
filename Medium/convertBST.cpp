/*
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is 
changed to the original key plus the sum of all keys greater than the original key in BST.
As a reminder, a binary search tree is a tree that satisfies these constraints:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1: [See diagram to better understand]
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Example 2:
Input: root = [0,null,1]
Output: [1,null,1]
*/





/*
Logic:
The question asks that all the greater nodes' values should be added to the current node. All the greater elements to the
current node is present in its right sub-tree. So, we traverse the right sub-tree first and then the left sub-tree (like 
a reverse inorder), maintaining a sum variable. We start from the rightmost leaf, which has the highest value and at this 
point the node's value won't change. As we go up in bottom-up manner from right to the root and then to it's left sub-tree, 
we keep adding adding the sum's value to the current node's value and send the current node's value as the sum variable.
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
    void RtoLtraversal(TreeNode *root, int &s){
        if(root==NULL){
            return;
        }
        
        RtoLtraversal(root->right,s);
        root->val+=s;
        s=root->val;
        RtoLtraversal(root->left,s);
        
        return;
    }
    
    TreeNode* convertBST(TreeNode* root) {
        int s=0;
        RtoLtraversal(root,s);
        
        return root;
    }
};