def split_and_join(line):
    # write your code here
    list_of_strings = line.split(" ")
    hyphen_separated_string = "-".join(list_of_strings)
    
    return hyphen_separated_string
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
