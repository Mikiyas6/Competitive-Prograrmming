class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = 0
        def recur(node):
            nonlocal res
            if not node: return True, inf, -inf, 0
            s1, mn1, mx1, sm1 = recur(node.left)
            s2, mn2, mx2, sm2 = recur(node.right)
            if s1 and s2 and mx1 < node.val < mn2: res = max(res, sm1+sm2+node.val)
            return s1 and s2 and mx1 < node.val < mn2, min(mn1, mn2, node.val), max(mx1, mx2, node.val), sm1+sm2+node.val
        recur(root)
        return res