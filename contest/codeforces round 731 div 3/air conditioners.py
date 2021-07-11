if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        i = input()
        n, k = list(map(int, input().split()))
        k_index = list(map(int, input().split()))
        k_value = list(map(int, input().split()))
        ref_dict = {k_index[i]: k_value[i] for i in range(k)}
        arr = []
        for j in range(n):
            arr.append(min([(ref_dict[x] + abs(x - (j+1))) for x in ref_dict.keys()]))
        print(' '.join(map(str, arr)))