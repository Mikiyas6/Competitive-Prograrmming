# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        def BFS(root):

            queue = deque([root])
            result = []

            while queue:

                level = len(queue)
                total = 0

                for _ in range(level):

                    node = queue.popleft()
                    total += node.val #I used the value that i popped from the queue

                    # I harvest the childs of the node if there are any
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    
                    #Moving on to the next node in the same level, which is the first node in the queue
                
                average = total/level
                result.append(average)
            
            return result

        return BFS(root)
                    
                

