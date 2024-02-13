class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:

        n = len(fronts)
        output = []

        defects = set()

        min_good_integer = float("inf")

        for i in range(n):

            if fronts[i] == backs[i]:

                defects.add(fronts[i])

        for card_number in fronts + backs:

            if card_number not in defects:

                min_good_integer = min(min_good_integer,card_number)

        return min_good_integer if min_good_integer != float("inf") else 0