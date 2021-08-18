if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    ref_dict = dict()
    for i in range(n):
        ref_dict[arr[i]] = i+1

    if len(ref_dict) >= k:
        print('YES')
        print(' '.join(map(str, list(ref_dict.values())[:k])))
    else:
        print('NO')