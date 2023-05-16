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
            while i < len(chars):
                if (i == len(chars) -1):
                    if counter == 1:
                        s += str(chars[i])
                    else:
                        s += str(chars[i]) + str(counter)
                        chars [i-counter + 1:i+1] = list(s)
                    break
                elif chars[i] == chars [i+1]:
                    counter += 1
                else:
                    if counter == 1:
                        s += str(chars[i])
                    else:
                        s += str(chars[i]) + str(counter)
                        chars [i-counter + 1:i+1] = list(s)
                        i -= (counter - 2)
                    counter = 1
                    s = ""
                i += 1
            return len(chars)  
            
