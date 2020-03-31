# Checks whether string ends with given ending
def solution(string, ending):
    for i in reversed(range(1, len(ending) + 1)):
        if ending[-i] != string[-i]:
            return False
    return True
    if ending == '':
        return True
    else:
        return False

# Test
print(solution('abcde', 'cde'))  # returns True
print(solution('abc', 'd'))  # returns False
