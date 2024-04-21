# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        current = self.head
        chosen_value = current.val
        index = 1

        while current:
            if random.randint(1, index) == 1:
                chosen_value = current.val
            current = current.next
            index += 1

        return chosen_value

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()