# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def count(nums):
            sorted_nums = sorted(nums)
            hashmap = defaultdict(int)
            count = 0
            for i in range(len(nums)):
                hashmap[nums[i]] = i
            for i in range(len(nums)):
                if sorted_nums[i] != nums[i]:
                    index = hashmap[sorted_nums[i]]
                    hashmap[nums[i]] = index
                    hashmap[nums[index]] = i
                    nums[index],nums[i] = nums[i],nums[index]
                    count += 1
            return count

        def bfs(root):
            queue = deque([root])
            counter = 0
            while queue:
                level = len(queue)
                nodes = []
                for _ in range(level):
                    node = queue.popleft()
                    nodes.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                if nodes:
                    counter += count(nodes)
            return counter
        
        return bfs(root)
                