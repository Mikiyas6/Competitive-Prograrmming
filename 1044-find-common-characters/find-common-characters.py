class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word = words[0]
        word = list(word)
        others = words[1:]
        lists = []
        for i in range(len(word)):
            flag = False
            for j in range(len(others)):
                if word[i] in others[j]:
                    listing = list(others[j])
                    listing.pop(others[j].index(word[i]))
                    others[j] = ''.join(listing)
                    flag = True
                else:
                    flag = False
                    break
            if flag == True:
                lists.append(word[i])
        return lists