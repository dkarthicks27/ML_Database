# limit building 1 to 10,000

# let us define boring appt as 1, 11, 111, 1111, (11111 wont make it as it > 10,000)
# 2, 22, 222, 2222
# 9, 99, 999, 9999

# so in each of that there are what is that number if it is one based then I have to know what is the len(of no)
# if it is 3

# then I would have 3 * (3 + 1) / 2 = 1 + 2 + 3
# if the number is say 44 then I am sure there is 3 pairs of n * (n +1) / 2
# so n = 777, then 6 * (4 * 5 / 2) = 6 * 10 = 60, and now 777 has len = 3
# 3 * (3 + 1) / 2 gives me 6 so total 66


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        n_len = len(str(n))
        m = int(str(n)[0])

        total = (m - 1) * 10 + (n_len * (n_len + 1))//2
        print(total)
