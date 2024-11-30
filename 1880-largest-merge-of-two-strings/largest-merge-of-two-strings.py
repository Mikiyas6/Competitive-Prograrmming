from collections import deque
class Solution:
    def largestMerge(self, w1: str, w2: str) -> str:
        res = []
        while w1 or w2:
            w1, w2 = sorted([w1, w2])
            res.append(w2[0])
            w2 = w2[1:]
        return "".join(res)
        