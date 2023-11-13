def reverseString(string):
    return string[::-1]


def reverse_string(string):
    reversed_str = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_str += string[i]
    return reversed_str


def reverse_string_mirror_idx(string):
    text = list(string)
    for i in range(len(string) // 2):
        mirror_idx = len(string) - 1 - i
        text[i], text[mirror_idx] = text[mirror_idx], text[i]
    return "".join(text)



def main():
    string = "hello"
    print(reverseString(string))
    print(reverse_string(string))
    print(reverse_string_mirror_idx(string))


if __name__ == "__main__":
    main()