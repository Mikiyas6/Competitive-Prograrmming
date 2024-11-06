# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        #Functin to find the middle of LinkedList
        def findMiddle(head):
            if not head or not head.next:
                return head
            slow = head
            fast = head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        #Function to reverse Linkedlist
        def reverse(head):
            prev = None
            current = head

            while current:
                next_node = current.next  
                current.next = prev       
                prev = current            
                current = next_node       

            return prev  

        def fun(list1,list2):
            if not list1:
                return list2
            if not list2:
                return list1
            
            segment1 = list1.next
            segment2 = list2.next
            list1.next = list2
            list2.next = fun(segment1,segment2)
            return list1
            
        
        middle = findMiddle(head)
        list2 = middle.next
        middle.next = None
        list1 = head

        reversed_list2 = reverse(list2)

        fun(list1,reversed_list2)