class Solution:
    def maxProduct(self, words: list[str]) -> int:
        words.sort(key=lambda x: len(x), reverse=True)
        best = 0
        bitsets = [0] * len(words)

        for i in range(len(words)):
            bitset = 0
            wlen = len(words[i])

            if wlen * len(words[0]) < best:
                return best

            for char in words[i]:
                bitset |= (1 << (ord(char) - ord('a')))

            for j in range(i):
                if (bitsets[j] & bitset) == 0:
                    best = max(best, wlen * len(words[j]))

            bitsets[i] = bitset

        return best