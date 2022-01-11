/*
Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.

Example 2:
Input: root = [4,3,null,1,2]
Output: 2
Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.

Example 3:
Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negatives. Return an empty BST.
*/






/*
Logic:
We define a class Info, which will keep track of the sum, the maximum, minimum of all the nodes below it and whether they,
including the current node form a BST (We follow the bottom-up recursive approach). If they form a BST, we take an account 
of the sum of all the nodes and keep a global variable to keep track of the maximum sum value. If they don't form a BST,
the 'ans' attribute keeps track of the maximum sum from the BST from either the left or right sub-tree.
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
    /*
    int sum=0;
    
    int helper(TreeNode *root,TreeNode* min,TreeNode* max){
        if(root==NULL)
            return 0;
        
        int left=helper(root->left,min,root);
        int right=helper(root->right,root,max);
        
        if((left==0 && root->left!=NULL) || (right==0 && root->right!=NULL))
            return 0;
        
        int s=left+right+root->val;
        if(s>sum)
            sum=s;
        cout<<"S :"<<s<<", "<<"Sum :"<<sum<<endl;
        if((min && root->val<min->val) || (max && root->val>max->val)){
            cout<<"Yo :"<<root->val<<endl;
            return 0;
        }
        
        return s;
    }
    */
    struct Info{
        int min;
        int max;
        int sum;
        int ans;
        bool isBST;
    };
    
    int sum=0;
    
    Info helper(TreeNode* root){
        if(root==NULL)
            return {INT_MAX,INT_MIN,0,0,true};
        if(root->left==NULL && root->right==NULL){
            sum=max(sum,root->val);
            return {root->val,root->val,root->val,root->val,true};
        }
        
        Info left=helper(root->left);
        Info right=helper(root->right);
        
        Info curr;
        curr.sum=left.sum+right.sum+root->val;
        
        if(left.isBST && right.isBST && (root->val>left.max) && (root->val<right.min)){
            curr.min=min(root->val,min(right.min,left.min));
            curr.max=max(root->val,max(right.max,left.max));
            
            curr.ans=curr.sum;
            sum=max(sum,curr.ans);
            curr.isBST=true;
            return curr;
        }
        curr.ans=max(right.ans,left.ans);
        curr.isBST=false;
        return curr;
    }
    
    int maxSumBST(TreeNode* root) {
        Info s=helper(root);
            
        return sum;
    }
};