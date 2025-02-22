# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.new_root = TreeNode(0)
        def construct(new_root,root):
            if not root:
                return None
            if root.left:
                node = TreeNode(2 * new_root.val + 1)
                new_root.left = construct(node,root.left)
            if root.right:
                node = TreeNode(2 * new_root.val + 2)
                new_root.right = construct(node,root.right)
            return new_root
        print(construct(self.new_root,self.root))

    def find(self, target: int) -> bool:
        def bfs(root,target):
            queue = deque([root])
            while queue:
                level = len(queue)
                for _ in range(level):
                    node = queue.pop()
                    if node.val == target:
                        return True
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return False
        
        return bfs(self.new_root,target)
                


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)