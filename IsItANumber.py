# Checks if input is a number 
def isDigit(string):
    try:
        float(string)
    except:
        return False
    return True

# Test
print(isDigit("2324.3")) # True
