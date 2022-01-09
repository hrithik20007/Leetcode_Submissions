/*
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique 
values from 1 to n. Return the answer in any order.

Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
Input: n = 1
Output: [[1]]
*/







/*
Logic:
Each no. from 1 to n, can act as a root node to all elements to its left (for left sub-tree root nodes) and all elements 
to its right (for right sub-tree root nodes). The left and right subtree root nodes' vectors are solved recursively. Each
right sub-tree root, left sub-tree root and current root(the i-th value node) is combined to give unique combinations of
BSTs. 
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
    vector<TreeNode*> helper(int start, int end){
        vector<TreeNode*> trees;
        if(start>end){
            trees.push_back(NULL);
            return trees;
        }
        if(start==end){
            TreeNode* node=new TreeNode(start);
            trees.push_back(node);
            return trees;
        }
        
        int i;
        for(i=start;i<=end;i++){
            
            /*vector<TreeNode*> left=helper(start,i-1);
            vector<TreeNode*> right=helper(i+1,end);
            
            for(j=0;j<left.size();i++){
                for(k=0;k<right.size();k++){
           */
            for (TreeNode *lt : helper(start, i-1)) {   //For traversing the vector made from the roots of the left elements
                for (TreeNode *rt : helper(i+1, end)) { // .... .....    .... ..... .... .... ... ....  ... .. right .....
                    //TreeNode* lt=left[j];
                    //TreeNode* rt=right[k];
                    TreeNode* node=new TreeNode(i);
                    node->left=lt;
                    node->right=rt;
                    trees.push_back(node);
                }
            }
        }
        
        return trees;
    }
    vector<TreeNode*> generateTrees(int n) {
        return helper(1,n);
    }
};