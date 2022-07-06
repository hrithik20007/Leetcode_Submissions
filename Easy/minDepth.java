/*
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
*/






/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int helper(TreeNode root,int l){
        if(root.left==null && root.right==null) return l;
        
        int a=Integer.MAX_VALUE,b=Integer.MAX_VALUE;
        if(root.left!=null) a=helper(root.left,l+1);
        if(root.right!=null) b=helper(root.right,l+1);
        
        return Math.min(a,b);
    }
    
    public int minDepth(TreeNode root) {
        if(root==null) return 0;
        if(root.left==null && root.right==null) return 1;
        
        return helper(root,1);
    }
}