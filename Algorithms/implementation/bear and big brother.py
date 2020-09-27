a, b = list(map(int, input().split()))
from math import log10
from math import floor
# count = 0
# while lim <= bob:
#     lim = lim * 3
#     bob = bob * 2
#     count += 1

count = (log10(b/a) / log10(1.5)) + 1

print(floor(count))
