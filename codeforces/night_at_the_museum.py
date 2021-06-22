import string

if __name__ == '__main__':
    inp = input()

    low = string.ascii_lowercase
    ref_dict = {low[i]: i+1 for i in range(26)}
    min_len = 0
    inp = 'a' + inp
    for i in range(len(inp) - 1):
        min_len += min(abs(ref_dict[inp[i]] - ref_dict[inp[i+1]]), 26 - abs(ref_dict[inp[i]] - ref_dict[inp[i+1]]))

    print(min_len)