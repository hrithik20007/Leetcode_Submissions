/*
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and 
(row + 1, col + 1) respectively. The root of the tree is at (0, 0). The vertical order traversal of a binary tree is a 
list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost 
column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.
Return the vertical order traversal of the binary tree.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.

Example 2:
Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.

Example 3:
Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.
*/







/*
Logic: We take a map of a map of vector. The first map maps the column with the second map, which maps row with vectors.
Thus, we have a vector for each (column,row) coordinate. These vectors store the node values present in that coordinate.
We go over all the nodes by DFS recursion approach and put all the nodes in the required 2D map positions. In the main
function, we go over them by creating an empty vector for each column and putting the map vector elements in that vector
(after sorting them first, since each node present in the same coordinate has to be sorted as well). These final vectors
are pushed into our main answer vector 'ans'.
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
    map<int,map<int,vector<int>>> v;
    vector<vector<int>> ans;
    
    void helper(TreeNode* root, int row, int col){
        if(root==NULL)
            return;
        
        v[col][row].push_back(root->val);
        
        helper(root->left,row+1,col-1);
        helper(root->right,row+1,col+1);
    }
    
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        if(root==NULL)
            return {};
        
        helper(root,0,0);
        
        for(auto it1:v){
            ans.push_back(vector<int> ());
            for(auto it2:it1.second){
                sort(it2.second.begin(),it2.second.end());
                for(auto it3:it2.second)
                    ans.back().push_back(it3);
            }
        }
        
        return ans;
    }
};
    
    
    
    
    
    
    
    
    
    
/*
map<int,vector<int>> v;
vector<vector<int>> ans;

void columns(TreeNode* root, int row, int col){
    if(root==NULL)
        return;

    v[col].push_back(root->val);

    columns(root->left,row+1,col-1);
    columns(root->right,row+1,col+1);
}

vector<vector<int>> verticalTraversal(TreeNode* root) {
    if(root==NULL)
        return {};

    columns(root,0,0);

    map<int,vector<int>>::iterator it;
    for(it=v.begin();it!=v.end();it++){
        sort(it->second.begin(),it->second.end());
        ans.push_back(it->second);
    }

    return ans;
*/