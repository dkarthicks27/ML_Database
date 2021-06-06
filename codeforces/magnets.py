v = [input() for i in range(int(input()))]
print(1 + sum(a != b for a, b in zip(v, v[1:])))


# py py is very slow so it is better to always compile using python rather than py py when it comes to codeforces
