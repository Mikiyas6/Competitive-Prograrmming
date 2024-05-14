# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        if not root:
            False
        
        def find_node(root,x):

            if not root:
                return root
            
            if root.val == x:
                return root
            
            left = find_node(root.left,x)

            if left:
                return left
            
            right = find_node(root.right,x)

            return right
        
        def find_depth(root,node,depth):

            if not root:
                return 0 
            if root == node:
                return depth
            
            left = find_depth(root.left,node,depth+1)

            right = find_depth(root.right,node,depth+1)

            return max(left,right)

        def is_siblings(root,node_x,node_y):

            if not root:
                return False
            
            if (root.left == node_x and root.right == node_y) or (root.left == node_y and root.right == node_x):
                return True
            return is_siblings(root.left,node_x,node_y) or is_siblings(root.right,node_x,node_y)

        node_x = find_node(root,x)
        node_y = find_node(root,y)

        depth_x = find_depth(root,node_x,0)
        depth_y = find_depth(root,node_y,0)

        print(depth_x,depth_y)

        if depth_x == depth_y and not is_siblings(root,node_x,node_y):
            return True
        return False