# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        # def BFS(root):

        #     if not root:
        #         return False
            
        #     queue = deque([root])
            
        #     while queue:

        #         level = len(queue)
        #         nodes = []

        #         for _ in range(level):

        #             node = queue.popleft()

        #             if not node:
        #                 nodes.append(None)
        #             else:
        #                 nodes.append(node.val)

        #                 if node.left:
        #                     queue.append(node.left)
        #                 else:
        #                     queue.append(None)

        #                 if node.right:
        #                     queue.append(node.right)
        #                 else:
        #                     queue.append(None)
                
        #         i, j = 0, len(nodes)-1

        #         while i <= j:

        #             if nodes[i] != nodes[j]:
        #                 return False
                    
        #             i += 1
        #             j -= 1
            
        #     return True
                        
        # return BFS(root)

        if not root:
            return root

        def fun(left_node,right_node):

            if not left_node and not right_node:
                return True
            if not left_node and right_node:
                return False
            if not right_node and left_node:
                return False
            
            return left_node.val == right_node.val and fun(left_node.left,right_node.right) and fun(left_node.right,right_node.left)
        
        return fun(root.left,root.right)