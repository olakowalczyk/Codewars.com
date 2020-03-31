# String formatting acocording to rule 'abcd' -> 'A-Bb-Ccc-Dddd'
def accum(s):
    text = []
    for i in range(len(s) + 1):
        phrase = (s[i - 1] * i).capitalize()
        text.append(phrase)
        result = '-'.join(text)
    return result[1:]


# Test
print(str(accum("abcd")))  # "A-Bb-Ccc-Dddd"
