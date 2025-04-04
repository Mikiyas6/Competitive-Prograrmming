# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hashmap = defaultdict(int)
        childs = set()
        for rootValue,childValue,side in descriptions:
            root = hashmap[rootValue] if hashmap[rootValue] else TreeNode(rootValue) 
            child = hashmap[childValue] if hashmap[childValue] else TreeNode(childValue)
            isLeft = True if side == 1 else False
            if isLeft:
                root.left = child
            else:
                root.right = child
            hashmap[rootValue] = root
            hashmap[childValue] = child
            childs.add(childValue)
        for rootValue,childValue,side in descriptions:
            if rootValue not in childs:
                return hashmap[rootValue]
        
        