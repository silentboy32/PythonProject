
def factorial(num):
    if (num == 0 or num == 1):
        return 1

    else:
        return num * factorial(num-1)
# 4 * 3 * 2 * 1  
re = factorial(4)
print(re)