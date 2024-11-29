class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        return sum(i == m for i, m in enumerate(itertools.accumulate(flips, max), 1))