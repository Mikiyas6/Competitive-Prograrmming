# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        current = head
        size = 0
        nums = []
        while current:
            size += 1
            nums.append(current.val)
            current = current.next
        result = [0]*size
        stack = []
        for i in range(size):
            while stack and nums[i] > nums[stack[-1]]:
                index = stack.pop()
                result[index] = nums[i]
            stack.append(i)
        return result
