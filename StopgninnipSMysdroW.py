# Returns the words in string with reversed words if they are eqaul or more than 5-chars
def spin_words(sentence):
    sentence = sentence.split(' ')
    result = ''
    for word in sentence:
        if len(word) >= 5:
            word = word[::-1]
        else:
            word = word
        result = result + ' ' + word
    return result.lstrip()


# Test
# string etirW consist string letter spaces spaces
print(spin_words("gnirts Write tsisnoc gnirts rettel secaps secaps"))
