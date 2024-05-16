# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return
        
        # Initialize the stack and push the root node
        stack = [root]
        prev = None
        
        while stack:
            # Pop the current node from the stack
            current = stack.pop()
            
            # If there's a previous node, adjust its pointers
            if prev:
                prev.left = None
                prev.right = current
            
            # Push the right and then left child to the stack
            # We push right child first so that left child is processed first
            # The value at the top of the stack is the next element in the preorder
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            
            # Update the previous node to the current node
            prev = current 


        
        