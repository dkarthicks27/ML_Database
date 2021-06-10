if __name__ == '__main__':
    n = int(input())
    li = list(map(int, input().split()))

    max_arr = max(li)
    min_arr = min(li)

    indexMax = li.index(max_arr)

    indexMin = len(li) - 1 - li[::-1].index(min_arr)

    if indexMax < indexMin:
        print(indexMax + len(li) - 1 - indexMin)

    else:
        print(indexMax - 1 + len(li) - 1 - indexMin)
