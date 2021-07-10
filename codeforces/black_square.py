# if __name__ == '__main__':
#     calorie_each_pos = input().split()
#     ref = {str(i+1): int(calorie_each_pos[i]) for i in range(len(calorie_each_pos))}
#     s = input()
#
#     count = 0
#     for i in s:
#         count += ref[i]
#
#     print(count)
from collections import OrderedDict

k = 'cir'
l = 'car'
arr = [set(k), set(l)]

res = set.intersection(*arr)
print(res)
new_arr = [0 for i in range(20)]
for i in res:
    new_arr[k.index(i)] = i

new_arr = [i for i in new_arr if i != 0]
output = ''.join(new_arr)
print(output)
while True:
    if output in k:
        print(output)
        break
    else:
        output = output[:-1]