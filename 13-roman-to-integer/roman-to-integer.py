class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = defaultdict(str)
        hashmap["I"] = 1
        hashmap["V"] = 5
        hashmap["X"] = 10
        hashmap["L"] = 50
        hashmap["C"] = 100
        hashmap["D"] = 500
        hashmap["M"] = 1000
        hashmap["CM"] = 900
        hashmap["XC"] = 90
        hashmap["IV"] = 4
        hashmap["IX"] = 9
        hashmap["XL"] = 40
        hashmap["CD"] = 400
        total = 0
        i = 0
        while i < len(s):
            if hashmap[s[i:i+2]]:
                value = hashmap[s[i:i+2]]
                i += 2
            else:
                value = hashmap[s[i]]
                i += 1
            total += value
        return total
