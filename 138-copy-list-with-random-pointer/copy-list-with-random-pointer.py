"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
     
        if not head:
            return None

        # Step 1: Create a mapping between original nodes and copied nodes
        mapping = {}
        node = head
        while node:
            mapping[node] = Node(node.val)
            node = node.next

        # Step 2: Update next and random pointers of copied nodes
        node = head
        while node:
            copied_node = mapping[node]
            if node.next:
                copied_node.next = mapping[node.next]
            if node.random:
                copied_node.random = mapping[node.random]
            node = node.next

        return mapping[head]
