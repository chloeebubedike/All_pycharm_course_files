def solution(S):
    string = S
    # create empty list to hold passwords
    list = []
    new_list = []
    # loop through every character in the string
    for character in string:
        if character.isdigit():
            char_index = S.index(character)
            list.append(string[:char_index])
            list.append(string[char_index + 1:])

    for item in list:
        for character in item:
            if character.isupper():
                new_list.append(character)
                new_list.append(item)

    if len(new_list) > 0:
        return len(new_list)
    else:
        return -1

    print(list)
    print(new_list)

solution("a0Ba")

# check if contains upper string
# check that it does not contain any digit

print("----")
index = "apples".index("p")

print("apples"[index:])