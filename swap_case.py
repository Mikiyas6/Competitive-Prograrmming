def swap_case(s):
    string = ""
    for letter in s:
        if letter.islower():
            string += letter.upper()
        elif letter.isupper():
            string += letter.lower()
        else:
            string += letter
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
