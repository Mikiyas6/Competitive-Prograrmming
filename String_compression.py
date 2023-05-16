class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s = ""
        counter = 1
        if len(chars) == 1:
            return 1
        else:
            i = 0
            pointer = 0
            while i < len(chars):
                if (i == len(chars) -1):
                    if pointer == i:
                        s += str(chars[i])
                    else:
                        s += str(chars[i]) + str(i - pointer + 1)
                        chars [pointer:i+1] = list(s)
                    break
                elif chars[i] == chars [i+1]:
                    pointer -= 1
                else:
                    if pointer == i:
                        s += str(chars[i])
                    else:
                        s += str(chars[i]) + str(i - pointer + 1)
                        chars [pointer:i+1] = list(s)
                        pointer += 1
                        i = pointer
                    s = ""
                i += 1
                pointer += 1
            return len(chars)  
            
