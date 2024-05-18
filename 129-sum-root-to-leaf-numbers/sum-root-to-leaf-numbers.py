# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def DFS(root,cumulative):

            if not root:
                return 0

            if not root.left and not root.right:
                result = (cumulative)*10 + root.val
                return result
            
            result = (cumulative)*10 + root.val
            
            return DFS(root.left,result) + DFS(root.right,result)

        return DFS(root,0)

##################################################################
        # total = 0

        # def store(string):

        #     nonlocal total
            
        #     string = "".join(string)
        #     total += int(string)
        
        # def DFS(root,string):

        #     if not root:
        #         return

        #     if not root.left and not root.right:
        #         store(string+[str(root.val)])
        #         return
            
        #     DFS(root.left,string+[str(root.val)])

        #     DFS(root.right,string+[str(root.val)])

        #     return

        # DFS(root,[])

        # return total

        



