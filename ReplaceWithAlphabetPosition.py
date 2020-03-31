# Returns the characters position in alphabet
import string
alphabet = string.ascii_lowercase
dic = {}
key = 1
for i in alphabet:
    dic[i] = key
    key += 1


def alphabet_position(text):
    result = ''
    text = text.lower()
    text = ''.join(c for c in text if c != ' ')
    for char in text:
        if char in alphabet:
            result += ' ' + str(dic.get(char))
    return result.lstrip()

# Test 
print(alphabet_position("The sunset sets at twelve o' clock."))

