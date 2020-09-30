n = list(input())
count = 0

for i in n:
    if i == '4' or i == '7':
        count += 1

a = list(str(count))
b = [1 if i == '4' or i == '7' else 0 for i in a]

if all(b):
    print('YES')
else:
    print('NO')
