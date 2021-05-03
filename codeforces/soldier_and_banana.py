if __name__ == '__main__':
    k, n, w = list(map(int, input().split()))

    costOfWBananas = k * (w * (w + 1)) // 2
    if costOfWBananas - n > 0:
        print(costOfWBananas - n)
    else:
        print(0)