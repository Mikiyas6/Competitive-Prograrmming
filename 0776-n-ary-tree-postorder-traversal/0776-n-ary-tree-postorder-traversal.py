"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        def fun(root):

            if not root:
                return
            
            children = root.children
            result = []
            for child in children:
                result.extend(fun(child))
            result.append(root.val)
            return result
        
        return fun(root)
                