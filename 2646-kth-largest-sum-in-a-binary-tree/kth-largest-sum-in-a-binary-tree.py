# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        def bfs(root):
            queue = deque([root])
            minHeap = []
            size = 0
            while queue:
                level = len(queue)
                total = 0
                for _ in range(level):
                    node = queue.popleft()
                    total += node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                if size == k:
                    if minHeap[0] < total:
                        heappushpop(minHeap,total)
                else:
                    heappush(minHeap,total)
                    size += 1
            return heappop(minHeap) if size == k else -1
        return bfs(root)