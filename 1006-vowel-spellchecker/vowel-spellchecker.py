class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        def devowel(word):
            return ''.join('*' if c in 'aeiou' else c for c in word)

        wordset = set(wordlist)
        cap_dict = {}
        vowel_dict = {}

        for word in wordlist:
            lower_word = word.lower()
            cap_dict.setdefault(lower_word, word)
            vowel_dict.setdefault(devowel(lower_word), word)

        def check_word(query):
            if query in wordset:
                return query
            lower_query = query.lower()
            if lower_query in cap_dict:
                return cap_dict[lower_query]
            devoweled_query = devowel(lower_query)
            if devoweled_query in vowel_dict:
                return vowel_dict[devoweled_query]
            return ""

        return [check_word(query) for query in queries]