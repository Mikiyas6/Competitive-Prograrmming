# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def DFS(queue,lists):
            if not queue:
                return lists
            new_list = []
            length = len(queue)
            for i in range(length):
                new_list.append(queue[0].val)
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                queue.pop(0)
            lists.append(new_list[-1])
            return DFS(queue,lists)
        if not root:
            return []
        return DFS([root],[])
        
