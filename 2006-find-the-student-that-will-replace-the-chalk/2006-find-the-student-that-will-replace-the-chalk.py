class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        n = len(chalk)

        total = sum(chalk)

        #number_of_cycles = total // k

        if k % total == 0:

            return 0

        remaining = k % total

        for index, value in enumerate(chalk):

            remaining -= value

            if remaining < 0:

                return index
        