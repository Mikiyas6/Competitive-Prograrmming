# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

#         def inbound(row,col):

#             return 0 <= row and row < n and 0 <= col and col < m

#         def is_safe(path,row,col,index,target):

#             if not inbound(row,col):
#                 return False
            
#             if path[row][col]:
#                 return False
            
#             if board[row][col] != target[index]:
#                 return False
            
#             return True
        
#         def fun(row,col,path,index,target):
            
#             if index == len(target):

#                 return True
            
#             if is_safe(path,row,col,index,target):

#                 path[row][col] = True

#                 up = fun(row-1,col,path,index+1,target)

#                 down = fun(row+1,col,path,index+1,target)

#                 left = fun(row,col-1,path,index+1,target)

#                 right = fun(row,col+1,path,index+1,target)

#                 path[row][col] = False

#                 return up or down or left or right
            
#             return False
        
#         n = len(board)
#         m = len(board[0])
#         result = set()

#         for target in words:
#             path = [[False]*m  for _ in range(n)]
#             flag = False
#             for i in range(n):
#                 for j in range(m):
#                     if fun(i,j,path,0,target):
#                         flag = True
#                         result.add(target)
#                         break
#                 if flag:
#                     break
        
#         return list(result)

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def build_trie(words):
            root = TrieNode()
            for word in words:
                node = root
                for char in word:
                    node = node.children[char]
                node.is_word = True
            return root

        def dfs(row, col, node, path, result):
            if node.is_word:
                result.add("".join(path))

            if not (0 <= row < rows and 0 <= col < cols) or board[row][col] not in node.children:
                return

            tmp, board[row][col] = board[row][col], '#'
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(row + dr, col + dc, node.children[tmp], path + [tmp], result)
            board[row][col] = tmp

        rows, cols = len(board), len(board[0])
        root = build_trie(words)
        result = set()

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root, [], result)

        return list(result)

