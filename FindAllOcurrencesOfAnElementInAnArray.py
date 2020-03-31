# Finds list indexes of n
def find_all(list, n):
    result = []
    for i in range(len(list)):
        if list[i] == n:
            result.append(i)
    return result

# Test
print(find_all([6, 9, 3, 4, 3, 82, 11], 3))  # [2, 4]
