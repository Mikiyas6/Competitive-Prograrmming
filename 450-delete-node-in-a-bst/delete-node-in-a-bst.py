# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def get_min(root):

            if not root or not root.left:
                return root
            
            return get_min(root.left)

        def delete_node(root,value):
            
            if not root:
                return root

            if root.val == value:

                if not root.left and not root.right:
                    return None
                
                if root.left and not root.right:
                    return root.left
                
                if not root.left and root.right:
                    return root.right
                
                else:

                    node = get_min(root.right)

                    root.val = node.val

                    root.right = delete_node(root.right,node.val)

                    return root

            if value < root.val:
                root.left = delete_node(root.left,value)
            else:
                root.right = delete_node(root.right,value)
            
            return root
            
        return delete_node(root,key)

