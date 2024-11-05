class Bit:

    def __init__(self, n: int) -> None:
        self.bit = [0 for _ in range(n + 1)]

    def update(self, i: int, val: int) -> None:
        i += 1
        while i < len(self.bit):
            self.bit[i] += val
            i += self._find_RSB(i)

    def prefix_sum(self, i: int) -> int:
        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= self._find_RSB(i)
        return s

    def _find_RSB(self, i: int) -> int:
        return i & -i


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = []
        shift = 10 ** 4
        bit = Bit(max(nums) + shift)
        for i in range(len(nums) - 1, -1, -1):
            counts.append(bit.prefix_sum(nums[i] + shift - 1))
            bit.update(nums[i] + shift, 1)
        return counts[::-1]