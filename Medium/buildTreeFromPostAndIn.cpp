/*
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is 
the postorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]
*/







/*
Logic: We start from the last index of postorder vector and search the respective elements in the inorder vector. At the
position where it is found, we divide the inorder vector along that position, for the left and right subtree respectively.
Now for the left and right subtree, the starting and ending indexes of the postorder vectors should also change to help
facilitate the process further down the recursion tree. 
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
    
    TreeNode* buildTreeHelper(vector<int>& postorder, vector<int>& inorder , int posStart ,int posEnd ,int inStart ,int inEnd ){
        if(posStart > posEnd )
            return NULL;
        
        int rootData = postorder[posEnd];
        TreeNode* root = new TreeNode(rootData);
        
        //searching for root index
        auto it = find(inorder.begin(), inorder.end(), rootData);
        int root_index = it - inorder.begin();
        
        //for recursively making right subtree
        int right_inorder_start = root_index +1;
        int right_inorder_end = inEnd ;
        int right_postorder_end = posEnd-1;
        int right_postorder_start = right_postorder_end - (right_inorder_end-right_inorder_start);
        
        //for recursively making left subtree
        int left_inorder_start = inStart ;
        int left_inorder_end = root_index - 1; 
        int left_postorder_start =posStart;
        int left_postorder_end = right_postorder_start-1;
    
        //creating left and right subtree
        root->right = buildTreeHelper(postorder ,inorder , right_postorder_start ,right_postorder_end, right_inorder_start , right_inorder_end );
        root->left = buildTreeHelper(postorder  ,inorder , left_postorder_start  , left_postorder_end , left_inorder_start ,left_inorder_end  );
   
        return root;
    }
    
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        TreeNode* root = buildTreeHelper(postorder ,inorder , 0 , postorder.size()-1, 0 , inorder.size()-1);
        
        return root;
    }
};







/*
class Solution {
public:
    int searching(vector<int>& inorder, int curr, int start, int end){
        int i,pos=-1;
        for(i=start;i<=end;i++){
            if(inorder[i]==curr)
                pos=i;
        }
        return pos;
    }
    
    TreeNode* build(int start, int end, vector<int>& postorder, vector<int>& inorder){
        static int k=postorder.size()-1;
        if(start>end)
            return NULL;
        
        int curr=postorder[k];
        k-=1;
        
        TreeNode* node=new TreeNode(curr);
        if(start==end)
            return node;
        
        int pos=searching(inorder, curr, start, end);
        node->right=build(pos+1,end,postorder,inorder);
        node->left=build(start,pos-1,postorder,inorder);
        return node;
    }
    
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int start=0;
        int end=inorder.size()-1;
        
        return build(start, end, postorder, inorder);
    }
};
*/