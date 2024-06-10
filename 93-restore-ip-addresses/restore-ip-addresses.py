class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        ipAdresses = []

        def isValidInteger(string):

            if len(string) > 1 and string[0] == '0':
                return False
            
            val = int(string)

            return 0 <= val and val <= 255

        def dfs(i,address):

            if i == len(s):
                if len(address) == 4:
                    add = address[:]
                    add = '.'.join(add)
                    ipAdresses.append(add)
                return

            if len(address) == 4:
                return
            
            for j in range(i,len(s)):

                string = s[i:j+1]

                if isValidInteger(string):

                    address.append(string)
                    dfs(j+1,address)
                    address.pop()
        
        dfs(0,[])

        return ipAdresses
