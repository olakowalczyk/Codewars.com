# Returns my_word anagrams form words in list
def anagrams(my_word, list):
    my_word = ''.join(sorted(my_word))
    anagrams = []

    for word in list:
        i = ''.join(sorted(word))
        if i == my_word:
            anagrams.append(word)
    return anagrams


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))  #  ['aabb', 'bbaa']


