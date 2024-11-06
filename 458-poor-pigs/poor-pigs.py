class Solution:
    def poorPigs(self, buckets: int, timeDetect: int, timeTest: int) -> int:
        return ceil(log2(buckets)/log2(timeTest//timeDetect+1))
        