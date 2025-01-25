class TrieNode:
  def __init__(self):
    self.children={}
    self.isEnd=False

class Trie:
  def __init__(self):
    self.root=TrieNode()
  
  def insert(self,word):
    curr=self.root
    for i in word:
      if i not in curr.children:
        curr.children[i]=TrieNode()
      curr=curr.children[i]
    curr.isEnd=True
  
  def startsWith(self,pre):
    curr=self.root
    res=[]
    for i in pre:
      if i not in curr.children:
        return []
      curr=curr.children[i]
    self.dfs(curr,res,pre)
    return res
    
  
  def dfs(self,root,res,pre):
    if len(res)==3:
      return res
    if root.isEnd:
      res.append(pre)
    for k in root.children:
      self.dfs(root.children[k],res,pre+k)
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans=[]
        products.sort()
        i=0
        j=len(products)-1
        prefix=''
        for k in range(len(searchWord)):
            prefix+=searchWord[k]
            word=[]
            while i<=j and prefix!=products[i][:k+1]:
                i+=1
            while j>=i and prefix!=products[j][:k+1]:
                j-=1
            s=i
            while len(word)!=3 and s<=j:
                word.append(products[s])
                s+=1
            ans.append(word)
        return ans

    # Trie Approach
    # def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    #     ans=[]
    #     products.sort()
    #     trie=Trie()
    #     pref=''
    #     for i in products:
    #         trie.insert(i)
    #     i=0
    #     for i in range(len(searchWord)):
    #         pref+=searchWord[i]
    #         ans.append(trie.startsWith(pref) ) 
    #     return ans
        