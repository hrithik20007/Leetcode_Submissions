/*
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that 
adding up all the values along the path equals targetSum.
A leaf is a node with no children.
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
    boolean helper(TreeNode root,int targetSum,int s){
        s+=root.val;
        if(targetSum!=s && root.left==null && root.right==null) return false;
        if(targetSum==s && root.left==null && root.right==null) return true;
        
        boolean a=false,b=false;
        if(root.left!=null) a=helper(root.left,targetSum,s);
        if(root.right!=null) b=helper(root.right,targetSum,s);
        
        if(a==true || b==true) return true;
        return false;
    }
    
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root==null) return false;
        //if(root.val==targetSum && root.left==null && root.right==null) return true;
        
        return helper(root,targetSum,0);
    }
}