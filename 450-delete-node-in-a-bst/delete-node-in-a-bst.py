# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def buildBST(root1,root2):
            self.result = []
            def serialize(root):
                if not root:
                    return
                self.result.append(root.val)
                serialize(root.left)
                serialize(root.right)
            serialize(root1)
            serialize(root2)
            self.result.sort()
            def helper(start,end,arr):
                if start > end:
                    return None
                mid = start + (end-start)//2
                root = TreeNode(arr[mid])
                root.left = helper(start,mid-1,arr)
                root.right = helper(mid+1,end,arr)
                return root
            return helper(0,len(self.result)-1,self.result)
        def helper(root):
            if not root:
                return None
            if root.val == key:
                return buildBST(root.left,root.right)
            root.left = helper(root.left)
            root.right = helper(root.right)
            return root
        return helper(root)