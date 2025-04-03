"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def postOrder(root):
            if not root:
                return None
            children = root.children
            result = []
            for child in children:
                result.extend(postOrder(child))
            result.append(root.val)
            return result
        return postOrder(root)