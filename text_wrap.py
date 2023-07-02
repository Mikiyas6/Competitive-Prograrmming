import textwrap

def wrap(string, max_width):
    sections = len(string)//max_width
    counter = 0
    stro = ""
    for i in range(sections):
        stro += (string[counter:max_width+counter]) + "\n"
        counter += max_width
    stro += (string[counter:]) + "\n"
    return stro

if __name__ == '__main__':
