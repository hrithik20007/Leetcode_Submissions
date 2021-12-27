/*
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is 
the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
*/






/*
Logic: We start from the 0-th index of preorder vector and search the respective elements in the inorder vector. At the
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
    TreeNode* buildTreeHelper(vector<int>& preorder, vector<int>& inorder , int preStart ,int preEnd ,int inStart ,int inEnd ){
        if(preStart > preEnd )
            return NULL;
        
        int rootData = preorder[preStart];
        TreeNode* root = new TreeNode(rootData);
        
        //searching for root index
        auto it = find(inorder.begin(), inorder.end(), rootData);
        int root_index = it - inorder.begin();
        
        //for recursively making left subtree
        int left_inorder_end = root_index - 1; 
        int left_inorder_start = inStart ;
        int left_preorder_start =preStart +1;
        int left_preorder_end = (left_preorder_start + left_inorder_end - left_inorder_start);
    
        //for recursively making right subtree
        int right_inorder_end = inEnd ; 
        int right_inorder_start = root_index +1;
        int right_preorder_start = left_preorder_end + 1;
        int right_preorder_end = preEnd ;
    
        //creating left and right subtree
        root->left = buildTreeHelper(preorder  ,inorder , left_preorder_start  , left_preorder_end , left_inorder_start ,left_inorder_end  );
        root->right = buildTreeHelper(preorder ,inorder , right_preorder_start ,right_preorder_end, right_inorder_start , right_inorder_end );
   
        return root;
    }
    
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        TreeNode* root = buildTreeHelper(preorder ,inorder , 0 , preorder.size()-1, 0 , inorder.size()-1);
        
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
    
    TreeNode* build(int start, int end, vector<int>& preorder, vector<int>& inorder){
        static int k=0;
        if(start>end)
            return NULL;
        
        int curr=preorder[k];
        k+=1;
        
        TreeNode* node=new TreeNode(curr);
        if(start==end)
            return node;
        
        int pos=searching(inorder, curr, start, end);
        node->left=build(start,pos-1,preorder,inorder);
        node->right=build(pos+1,end,preorder,inorder);
        return node;
    }
    
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int start=0;
        int end=inorder.size()-1;
        
        return build(start, end, preorder, inorder);
    }
};
*/