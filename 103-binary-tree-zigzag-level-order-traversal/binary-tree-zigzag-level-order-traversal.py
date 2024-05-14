# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        def BFS(root):

            queue = deque([root])
            result = []
            depth = 0

            while queue:

                level = len(queue)
                nodes = []

                for _ in range(level):

                    if depth %2 == 0:

                        node = queue.popleft()
                        nodes.append(node.val)

                        if node.left:
                            queue.append(node.left)
                        if node.right:
                            queue.append(node.right)
        
                    else:

                        node = queue.pop()
                        nodes.append(node.val)

                        if node.right:
                            queue.appendleft(node.right)
                        if node.left:
                            queue.appendleft(node.left)
                
                print(nodes)
                depth += 1
                
                result.append(nodes)
            
            return result

        return BFS(root)

        # if not root:
        #     return []

        # def BFS(root):

        #     queue = deque([root])
        #     result = []
        #     flag = False

        #     while queue:

        #         level = len(queue)
        #         nodes = []

        #         for _ in range(level):

        #             node = queue.popleft()
        #             nodes.append(node.val)

        #             if node.left:
        #                 queue.append(node.left)
        #             if node.right:
        #                 queue.append(node.right)
                    
                
        #         if flag:
        #             nodes = nodes[::-1]
        #         flag = not flag
                
        #         result.append(nodes)
            
        #     return result

        # return BFS(root)