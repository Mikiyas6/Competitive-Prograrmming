# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def DFS(root,path):
            if not root:
                return []
            if not root.left and not root.right:
                path = path + [str(root.val)]
                return [''.join(path)]

            list1 = DFS(root.left,path+[str(root.val)+'->'])
            list2 = DFS(root.right,path+[str(root.val)+'->'])
            return list1+list2
        
        return DFS(root,[])