# IQ test - Finding position of number not matching the others (even or odd one)
def iq_test(numbers):
    numbers = numbers.split(' ')
    even = []
    odd = []
    for i in numbers:
        if int(i) % 2 == 0:
            even.append(i)
        elif int(i) % 2 != 0:
            odd.append(i)
    if len(odd) > len(even):
        return numbers.index(*even) + 1
    else:
        return numbers.index(*odd) + 1

# Test
print(iq_test("1 3 4 5")) # position 3: 4
