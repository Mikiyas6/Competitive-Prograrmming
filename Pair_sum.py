# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        sum = 0
        lists = []
        counter = 0
        current = head
        while (current != None):
            lists.append(current.val)
            current = current.next
        for i in range(len(lists)/2):
            if (i == 0):
                sum += lists[i] + lists[len(lists) - 1 -i]
            elif (lists[i] + lists[len(lists) -1 -i] > sum):
                sum = lists[i] + lists[len(lists)-1-i]
        return sum
            






