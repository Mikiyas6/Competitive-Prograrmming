class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        hashmap = defaultdict(int)
        initials = []

        index = 0
        for start,end in intervals:

            hashmap[start] = index
            initials.append(start)
            index += 1
        
        sorted_intervals = sorted(intervals)
        initials.sort()
        n = len(initials)

        result = []

        for start,end in intervals:

            idx = bisect.bisect_left(initials,end)

            if idx == n:
                result.append(-1)
               
            else:
                value = initials[idx]
                result.append(hashmap[value])
                
        return result


