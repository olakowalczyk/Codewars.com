# Gets middle character(s) from string
def get_middle(s):
    if len(s) % 2 != 0:
        return s[int(len(s) / 2)]
    else:
        return s[int(len(s) / 2) - 1: int(len(s) / 2 + 1)]

# Test
print(get_middle('test'))
print(get_middle('testing'))
