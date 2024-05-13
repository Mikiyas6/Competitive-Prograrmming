# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        def BFS(root,level):

            if not root:
                return
            
            if len(result) == level:
                result.append([])
            
            result[level].append(root.val)
            BFS(root.left,level+1)
            BFS(root.right,level+1)
            return 
        
        result = []
        BFS(root,0)
        average = []

        for level in result:
            mean = sum(level)/len(level)
            average.append(mean)
        
        return average
