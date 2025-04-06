# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def isCritical(prev,current):
            return (current.val < prev.val and current.val < current.next.val) or (current.val > prev.val and current.val > current.next.val)
        current = head.next
        prev = head
        critical_point = None
        min_point = float('inf')
        max_point = float('-inf')
        min_distance = float('inf')
        distance = 2
        while current.next:
            if isCritical(prev,current):
                min_point = min(min_point,distance)
                max_point = max(max_point,distance)
                min_distance = min(min_distance,distance-critical_point) if critical_point else float('inf')
                critical_point = distance
            prev = prev.next
            current = current.next
            distance += 1
        if min_point == float('inf') or max_point == float('-inf') or min_point == max_point:
            return [-1,-1]
        return [min_distance,max_point-min_point]

            


