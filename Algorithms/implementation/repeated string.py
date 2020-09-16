s = 'aba'
n = 10
import re

length = len(s)
reps, remainder = divmod(n, length)
print('reps: ', reps, '\nremainder: ', remainder)

new = s[:remainder]
print('remaining string: ', new)

total = len(re.findall('a', s)) * reps + len(re.findall('a', new))
print('total: ', total)


