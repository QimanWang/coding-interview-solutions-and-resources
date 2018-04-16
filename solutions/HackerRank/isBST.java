public class isBST {
    //The Node class is defined as follows:
    class Node {
        int data;
        Node left;
        Node right;
    }

    boolean checkBST(Node root, int min, int max) {
        if (root == null) {
            return true;
        }//base case the tree is null, which means the tree is valid because there is no data.
        // the root can also be null if the left most node is reached,
        //because the child of a leaf node is null.
        //if the recursion reached the leaf node, that means the tree is vaild for that side.
        if (root.data < min || root.data > max) {
            return false;
        }// if we are going left, the data can be any value less than the root or greater than equal to the smallest integer

        return checkBST(root.left, min, root.data - 1) && checkBST(root.right, root.data + 1, max);
        //this recursion will check down both side of the current node.
        //if anyside fails, it will return false.
        //the min and max value will update depends on the data value of the current node
        //if we going left, we update the max because the the max cannot be the same value as parent,
        //the value should be atleast  1 smaller.
        //if we going right, we update the min because the the min cannot be the same value as parent,
        //the value should be at least 1 larger.

    }//checkBST

    boolean checkBST(Node root) {
        return checkBST(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }//recursion pass in root , min and max value the root.data can be

}