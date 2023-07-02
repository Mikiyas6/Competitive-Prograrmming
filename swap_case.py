def swap_case(s):
    new_string = ""
    for character in s:
        if character.isupper():
            new_string += (character.lower())
        elif character.islower():
            new_string += (character.upper())
        else:
            new_string += (character)
    return new_string

if __name__ == '__main__':
