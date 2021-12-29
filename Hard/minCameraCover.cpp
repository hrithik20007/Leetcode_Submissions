/*
You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its 
parent, itself, and its immediate children.
Return the minimum number of cameras needed to monitor all nodes of the tree.

Example 1:
Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

Example 2:
Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid 
configurations of camera placement.
*/






/*
Logic: 
1-> Camera needs to be installed at the present node
2-> Camera needs not be installed
3-> Camera installed at the previous node
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
    int cameras=0;
    
    int helper(TreeNode* root){
        if(root==NULL)
            return 2;
        
        int left=helper(root->left);
        int right=helper(root->right);
        
        if(left==1 || right==1){            //1 carries the most preference when it comes to determining the outcome
            cameras+=1;
            return 3;
        }
        if(left==3||right==3)               //3 carries more preference to 2 when determining the value to be returned to
            return 2;                       //the next upper node
        if(left==2||right==2)
            return 1;
        
        return 0;
    }
    
    int minCameraCover(TreeNode* root) {
         if(helper(root)==1)
             cameras+=1;
        
        return cameras;
    }
};