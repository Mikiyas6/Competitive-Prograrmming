class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        result = deque()

        for _ in range(n - 1, -1, -1):
            if result:
                result.appendleft(result.pop())

            result.appendleft(deck[_])

        return list(result)