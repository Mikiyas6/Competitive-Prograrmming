class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time_to_live = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.time_to_live

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.time_to_live

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum(1 for token_time in self.tokens.values() if token_time > currentTime)

    # def __init__(self, timeToLive: int):

    #     self.time_to_live = timeToLive
    #     self.hashmap = defaultdict(int)
    #     self.frequency = defaultdict(int)
        
    # def generate(self, tokenId: str, currentTime: int) -> None:

    #     old_time_to_live = self.hashmap[tokenId]

    #     if old_time_to_live > 0:

    #         self.frequency[old_time_to_live] -= 1
        
    #     self.hashmap[tokenId] = currentTime + self.time_to_live

    #     new_frequency = self.hashmap[tokenId]

    #     self.frequency[currentTime + self.time_to_live] += 1

    # def renew(self, tokenId: str, currentTime: int) -> None:

    #     if tokenId in self.hashmap:

    #         if self.hashmap[tokenId] <= currentTime:

    #             old_time_to_live = self.hashmap[tokenId]

    #             if old_time_to_live > 0:

    #                 self.frequency[old_time_to_live] -= 1
                
    #             self.hashmap[tokenId] = currentTime + self.time_to_live

    #             new_frequency = self.hashmap[tokenId]

    #             self.frequency[currentTime + self.time_to_live] += 1

    # def countUnexpiredTokens(self, currentTime: int) -> int:
        
    #     counter = 0

    #     for frequency in self.frequency.keys():

    #         if frequency > currentTime:

    #            counter += 1
        
    #     return counter

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)