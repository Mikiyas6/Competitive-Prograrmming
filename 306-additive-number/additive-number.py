class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        if len(num) <= 2:
            return False
        
        def fun(i,part):
            if i == len(num):
                if len(part) < 3:
                    return False
                # if len(part) < 3:
                #     return False

                # j, k = 0, 1
                # while k+1 < len(part):
                #     if part[j] + part[k] != part[k+1]:
                #         return False

                #     j += 1
                #     k += 1

                return True

            for j in range(i,len(num)):
                string = num[i:j+1]
                if len(string) > 1 and string[0] == '0':
                    continue
                val = int(string)
                if len(part) >= 2 and part[-1] + part[-2] != val:
                    continue
                part.append(val)
                if fun(j+1,part):
                    return True
                part.pop()
            
            return False

        return fun(0,[])
            


