# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root,lists):
            if not root:
                return lists
            lists = inorder(root.left,lists)
            lists.append(root.val)
            lists = inorder(root.right,lists)
            return lists
        lists = inorder(root,[])
        maximum = 0
        listings = []
        for i in range(len(lists)):    
            count = lists.count(lists[i])
            listings.append([lists[i],count])
            maximum = max(maximum,count)
        new_list = []
        for i in range(len(listings)):
            if listings[i][1] == maximum and listings[i][0] not in new_list:
                new_list.append(listings[i][0])
        return new_list
        
