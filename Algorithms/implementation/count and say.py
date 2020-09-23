def next_term(s):
    i = 0
    result = []
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)


p = '1'
n = 10
for i in range(1, n):
    p = next_term(p)


print(p)