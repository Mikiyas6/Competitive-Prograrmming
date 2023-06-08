# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        lists = []
        while current != None:
            lists.append(current.val)
            current = current.next
        for i in range(1,len(lists)):
            pointer = i
            for j in range(i-1,-1,-1):
                if lists[pointer] < lists[j]:
                    self.swap(lists,j,pointer)
                    pointer -= 1
                else:
                    break
        current = head
        for i in range(len(lists)):
            current.val = lists[i]
            current = current.next
        return head
    def swap(self,lists,x,y):
        temp = lists[x]
        lists[x] = lists[y]
        lists[y] = temp
