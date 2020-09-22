def plusOne(digits):
    value = int(''.join(list(map(str, digits)))) + 1
    return list(map(int, str(value)))


k = plusOne([12])
print(k)