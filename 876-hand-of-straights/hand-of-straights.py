class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        # Count the frequency of each card
        card_count = Counter(hand)
        
        # Use a min-heap to get the smallest card to start forming groups
        min_heap = list(card_count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]
            for i in range(first, first + groupSize):
                if card_count[i] == 0:
                    return False
                card_count[i] -= 1
                if card_count[i] == 0:
                    # Remove the card from the heap if its count reaches zero
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)

        return True