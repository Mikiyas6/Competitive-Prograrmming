# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def bfs(root):
        
            if not root:
                return True

            left_queue = deque([root.left])
            right_queue = deque([root.right])

            while left_queue and right_queue:
                left_node = left_queue.popleft()
                right_node = right_queue.popleft()

                if not left_node and not right_node:
                    continue
                if not left_node or not right_node or left_node.val != right_node.val:
                    return False

                left_queue.append(left_node.left)
                left_queue.append(left_node.right)
                right_queue.append(right_node.right)
                right_queue.append(right_node.left)

            return True
            
        return bfs(root)
        # def DFS(queue,lists):
        #     if not queue:
        #         return lists
        #     new_list = []
        #     length = len(queue)
        #     for i in range(length):
        #         if queue[0]:
        #             new_list.append(queue[0].val)
        #             if queue[0].left:
        #                 queue.append(queue[0].left)
        #             else:
        #                 queue.append(None)
        #             if queue[0].right:
        #                 queue.append(queue[0].right)
        #             else:
        #                 queue.append(None)
        #         else:
        #             new_list.append(None)
        #         queue.pop(0)
        #     if not anagramChecker(new_list,0,len(new_list)-1):
        #         return False
        #     lists.append(new_list)
        #     return DFS(queue,lists)
        # def anagramChecker(lists,left,right):
        #     if left > right:
        #         return True
        #     if lists[left] == lists[right]:
        #         return anagramChecker(lists,left+1,right-1)
        #     else:
        #         return False
        # return DFS([root],[])
