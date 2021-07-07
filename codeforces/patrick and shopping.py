if __name__ == '__main__':
    d1, d2, d3 = list(map(int, input().split()))
    c1 = d1 + d3 + d2
    c2 = d1 + 2 * d3 + d1
    c3 = d2 + 2 * d3 + d2
    c4 = 2 * d2 + 2 * d1
    print(min(c1, c2, c3, c4))
