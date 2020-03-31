# Sums all the numbers in given range
def get_sum(a, b):
    sum = 0
    if a < b:
        for i in range(a, b + 1):
            sum += i
        return sum
    elif a > b:
        for i in range(b, a + 1):
            sum += i
        return sum
    else:
        return a


# Test
print(get_sum(5, 3))  # 3 + 4 + 5 = 12
