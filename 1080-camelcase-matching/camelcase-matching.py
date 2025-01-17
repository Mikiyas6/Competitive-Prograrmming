class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
      def matches(query,pattern):
        j=0
        for i in range(len(query)):
          if j<len(pattern) and query[i] == pattern[j]:
            j+=1
          elif query[i].isupper():
            return False
        return j==len(pattern)
      return [matches(query,pattern) for query in queries]



        