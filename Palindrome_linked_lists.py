# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        elif not head.next:
            return True
        elif not head.next.next:
            if head.val == head.next.val:
                return True
            else:
                return False
        else:
            # Finding the middle node
            slow = head
            fast = head
            while fast and fast.next:
                previous = slow
                slow = slow.next
                fast = fast.next.next
            # Finding the length of the Linked List
            current = head
            counter = 0
            while current:
                counter += 1
                current = current.next
            # Deciding path based on the length of the Linked List
            new_head = None
            if counter %2 == 0:
                new_head = slow
                previous.next = None
            else:
                new_head = slow.next
                previous.next = None
            # Reversing the new Linked List
            previous_node = None
            current_node = new_head
            while current_node:
                if not previous_node and not current_node.next:
                    previous_node = current_node
                    break
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node
            new_head = previous_node
            # Comparing corresponding values inside the two Linked Lists
            current1 = head
            current2 = new_head
            while current1 and current2:
                if current1.val != current2.val:
                    return False
                current1 = current1.next
                current2 = current2.next
            return True


    
