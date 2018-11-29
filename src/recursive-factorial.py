def factor(number):
    if number == 1:
        return 1
    else:
        return number * factor(number - 1)

print(factor(5))