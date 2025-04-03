"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        def postOrder(root):
            nonlocal result
            if not root:
                return
            children = root.children
            for child in children:
                postOrder(child)
            result.append(root.val)
        postOrder(root)
        return result