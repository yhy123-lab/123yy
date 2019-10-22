迭代
class Solution {
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if (t2 == null){
            return t1;
        }
        if (t1 == null){
            return t2;
        }
        Stack<TreeNode> stack1 = new Stack<>();
        Stack<TreeNode> stack2 = new Stack<>();
        stack1.push(t1);
        stack2.push(t2);
        while (!stack1.isEmpty()){
            TreeNode node1 = stack1.pop();
            TreeNode node2 = stack2.pop();
            node1.val += node2.val;
            if (node1.left != null && node2.left != null){
                stack1.push(node1.left);
                stack2.push(node2.left);
            }
            else if(node2.left != null){
                node1.left = node2.left;
            }
            if (node1.right != null && node2.right != null){
                stack1.push(node1.right);
                stack2.push(node2.right);
            }
            else if(node2.right != null){
                node1.right = node2.right;
            }
        }
        return t1;
    }
}

递归
class Solution {
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if (t2 == null){
            return t1;
        }
        if (t1 == null){
            return t2;
        }
        t1.val += t2.val;
        t1.left = mergeTrees(t1.left,t2.left);
        t1.right = mergeTrees(t1.right,t2.right);
        return t1;
    }
}
