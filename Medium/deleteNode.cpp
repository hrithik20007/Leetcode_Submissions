/*
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node 
reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
Search for a node to remove.
If the node is found, delete the node.

Example 1:
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:
Input: root = [], key = 0
Output: []
*/






/*
Logic:
At first, we reach the required node. It will have three cases-
1) Leaf- return NULL to the parent node
2) Only one sub-tree- return the sub-tree head
3) Two sub-trees present - copy the value of the leftmost leaf of the right sub-tree to the current node. Then delete 
                            the last leaf by calling the function again, but for that leaf node's value.
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
   TreeNode* deletenode(TreeNode* root, int key){
        if(root==NULL)
            return NULL;
        
        if(key<root->val)
            root->left=deletenode(root->left,key);
        else if(key>root->val)
            root->right=deletenode(root->right,key);
        else{
            if(root->left==NULL && root->right==NULL)
                return NULL;
            else if(root->left==NULL)
                return root->right;
            else if(root->right==NULL)
                return root->left;
            
            //Both left and right sub-trees exist
            TreeNode *temp=root->right;
            while(temp->left!=NULL)
                temp=temp->left;
            root->val=temp->val;
            root->right=deletenode(root->right,temp->val);
        }
        return root;
    }
    
    TreeNode* deleteNode(TreeNode* root, int key) {
        root=deletenode(root,key);
        
        return root;
    }
};