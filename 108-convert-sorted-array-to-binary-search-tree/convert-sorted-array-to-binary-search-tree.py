# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        # def rotate_left(root):

        #     p = root
        #     c = p.right
        #     g = c.right
        #     t2 = c.left

        #     c.left = p
        #     p.right = t2

        #     return c
        
        # def rotate_right(root):

        #     p = root
        #     c = p.left
        #     g = c.left
        #     t2 = c.right

        #     c.right = p
        #     p.left = t2

        #     return c

        # def find_height(root):

        #     if not root:
        #         return -1
            
        #     left_height = find_height(root.left)
        #     right_height = find_height(root.right)

        #     return max(left_height,right_height) + 1

        def BST(nums,s,e):

            if not nums or s > e:
                return None
            
            mid = s + (e-s)//2

            root = TreeNode(nums[mid])

            root.left = BST(nums,s,mid-1)
            root.right = BST(nums,mid+1,e)

            return root

        return BST(nums,0,len(nums)-1)
            
        
                

            



