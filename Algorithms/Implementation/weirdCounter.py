import math
tn = int(input())
n = math.floor(math.log2((tn + 2) / 3) + 1)

print("tn: ", tn)
print("\n")

def calc_tn(n):
    return 3 * pow(2, (n - 1)) - 2


def calc_val(n):
    return 3 * pow(2, n - 1)


key = calc_tn(n)
val = calc_val(n)
print("key: ", key)
print("val: ", val)


print("final result: ", val)
print("Below is the comparison: \n")
difference = abs(key-tn)
print("tn - key: ", tn - key)
print("val - (tn - key): ", val - difference)