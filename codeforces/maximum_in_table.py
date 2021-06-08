def recursive_sum(i, j):
    if i == 1 or j == 1:
        return 1
    else:
        return recursive_sum(i - 1, j) + recursive_sum(i, j - 1)


if __name__ == '__main__':
    n = int(input())
    print(recursive_sum(n, n))
