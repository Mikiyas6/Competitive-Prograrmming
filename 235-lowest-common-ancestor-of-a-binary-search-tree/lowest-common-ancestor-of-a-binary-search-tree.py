# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


            #            3

            #     5             1

            # 6       2      0      8

            #     7      4

        def DFS(root,p,q):

            if not root:
                return root
            if root == p or root == q: # p = 3 and q = 8
                return root

            if p.val < root.val and q.val < root.val:

                return DFS(root.left,p,q)

            elif p.val > root.val and q.val > root.val:

                return DFS(root.right,p,q)
            
            return root

            # if left and right: # p = 5 and q = 8
            #     return root
            
            # if not right: # p = 5 and q = 4
            #     return left
            
            # return right
        
        return DFS(root,p,q)