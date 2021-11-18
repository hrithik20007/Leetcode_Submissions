/*
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
*/





/*
Logic: We are using recursion to solve this, employing two pointers. We call the boolean recursive function, once passing
the left node of left node and the right node of right node. The other time we pass the right node of the left node and
the left node of the right node. We then check if their values are equal or not. If equal, it means the BT is symmetric.
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
    bool isMirror(TreeNode* r1, TreeNode* r2){
        if(r1==NULL && r2==NULL) return true;
        if(r1==NULL || r2==NULL) return false;
        
        return (r1->val == r2->val) && isMirror(r1->left,r2->right) && isMirror(r1->right,r2->left);
    }
    
    bool isSymmetric(TreeNode* root) {
        return isMirror(root,root);
    }
};