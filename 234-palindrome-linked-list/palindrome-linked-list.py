# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return head
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

        #Find the middle and break it in half
        middle = findMiddle(head)
        second_part = middle.next
        middle.next = None
        first_part = head

        # Reverse the second part
        reversedList = reverse(second_part)
        
        # Use two pointers to check the value in each node
        ptr1 = first_part
        ptr2 = reversedList

        while ptr1 and ptr2:
            if ptr1.val != ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return True

