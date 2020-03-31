# Returns minimum jump length to jump over the arr numbers
def avoid_obstacles(arr):
    min_jump = min(arr)
    while any(number % min_jump == 0 for number in arr):
        min_jump += 1
    return min_jump

# Test
print(avoid_obstacles([1, 4, 10, 6, 2]))  #  7
