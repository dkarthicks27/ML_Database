if __name__ == '__main__':
    ref_dict = dict()
    n = int(input())
    for i in range(n):
        ref_dict[i + 1] = sum(list(map(int, input().split())))

    tot = ref_dict[1]

    arr = list(sorted(ref_dict.items(), key=lambda kv: kv[1], reverse=True))

    for i, k in enumerate(arr):
        if k[1] == tot:
            print(i+1)
            break
