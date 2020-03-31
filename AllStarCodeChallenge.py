# Counts string occurence in phrase
def str_count(phrase, string):
    if string in phrase:
        return phrase.count(string)
    else:
        return 0

# Test
print(str_count("Hello", "ll"))
