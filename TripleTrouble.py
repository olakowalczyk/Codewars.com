# Interate on strings and marge chars starting wiith one[0] and ending with three[n]
# Strings are the same length


def triple_trouble(one, two, three):
    text = ''
    for i in range(len(one)):
        text = text + str(one[i]) + str(two[i]) + str(three[i])
    return text


# Test
print(triple_trouble("aaa", "bbb", "ccc"))  # abcabcabc
