/*
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
*/







/*
Logic: Same as level order traversal, however we keep a count variable to see whether the level no. is even or odd. If
even, we reverse the elements of 'l' vector before pushing into the 'ans' vector.
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
    
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if(root==NULL)
            return ans;
        
        int f=0;
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
                f+=1;
                if(f%2==1)
                    ans.push_back(l);
                else{
                    reverse(l.begin(),l.end());
                    ans.push_back(l);
                }
                l.clear();
                if(!q.empty())
                    q.push(NULL);
            }
        }
        
        return ans;
    }
};