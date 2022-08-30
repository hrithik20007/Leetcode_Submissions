/*
Logic:
We created a new root node and then used recursion to make the original treenode's left node as the new right node and 
vice-versa.
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
    public TreeNode invertTree(TreeNode root) {
        if(root==null || (root.left==null && root.right==null)) return root;
        TreeNode newroot = new TreeNode();
        newroot.val=root.val;
        newroot.left=invertTree(root.right);
        newroot.right=invertTree(root.left);
        return newroot;
    }
}