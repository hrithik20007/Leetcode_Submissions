/*
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level 
by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
*/







/*
Logic: We use a queue to input all the current level elements, followed by a NULL. We repeat this for every level, until
the final level, where after NULL there wouldn't be any elements left. All the current level elements are input into a
vector 'l'. After completion of each level, this vector is pushed into another global vector called 'ans'. After the final
level, we return this 'ans' vector.
*/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *    TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> ans;
    
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(root==NULL)
            return ans;
        
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
                ans.push_back(l);
                l.clear();
                if(!q.empty())
                    q.push(NULL);
            }
        }
        
        return ans;
    }
};