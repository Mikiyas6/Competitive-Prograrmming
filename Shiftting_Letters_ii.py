class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        offset = 26
        lists1 = []
        lists2 = [0] * (len(s)+1)
        prefix_sum = [0] * len(s)
        string = ""
        string1 = "abcdefghijklmnopqrstuvwxyz"
        # We represented lower case characters with their index 
        # we will pick one character from s, trace it in string1, and store its index in lists1
        for character in s:
            lists1.append(string1.index(character))
        # Doing the side_line algorithm to do prefix sum
        for value in shifts:
            start = value[0]
            end = value[1]
            direction = value[2]
            if direction == 0:
                lists2[start] -= 1
                lists2[end+1] += 1
            else:
                lists2[start] += 1
                lists2[end+1] -= 1
        # Doing the prefix sum
        for i in range(len(lists2)-1):
            prefix_sum[i] = prefix_sum[i-1] + lists2[i]
        # 
        for i in range(len(prefix_sum)):
            if prefix_sum[i] < 0:
                string += string1[(lists1[i] + prefix_sum[i] + offset) % offset]
            else:
                string += string1[(lists1[i] + prefix_sum[i]) % offset]
        return string        
