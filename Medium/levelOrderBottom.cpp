/*
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to 
right, level by level from leaf to root).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
*/







/*
Logic: Same as reversing the final ans vector, but implemented using a stack.
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
    vector<vector<int>> ans;
    
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        if(root==NULL)
            return ans;
        
        stack<vector<int>> s;
        queue<TreeNode*> q;
        q.push(root);
        q.push(NULL);
        
        vector<int> l;
        
        while(!q.empty()){
            TreeNode *node= q.front();
            q.pop();

            if(node!=NULL){
                l.push_back(node->val);

                if(node->left!=NULL)
                    q.push(node->left);
                if(node->right!=NULL)
                    q.push(node->right);
            }
            else{
                s.push(l);                      //Temporary vectors pushed into stack rather than ans
                l.clear();
                if(!q.empty())
                    q.push(NULL);
            }
        }
        
        while(!s.empty()){                      //New portion
            ans.push_back(s.top());
            s.pop();
        }
        
        return ans;
    }
};