class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        
        self.size = len(times)
        self.persons = persons
        self.times = times
        self.hashmap = defaultdict(int)
        self.winner_person = -1
        self.winner_count = -1
        self.result = []

        for person in persons:

            self.hashmap[person] += 1

            if self.hashmap[person] >= self.winner_count:
                self.winner_person = person
                self.winner_count = self.hashmap[person]
            
            self.result.append(self.winner_person)

    def q(self, t: int) -> int:

        idx = bisect.bisect_left(self.times,t)

        if idx == self.size:
            return self.result[-1]

        if t == self.times[idx]:
            return self.result[idx]

        return self.result[idx-1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)