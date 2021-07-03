if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        odd_arr = []
        even_arr = []
        for i in arr:
            if i % 2 == 0:
                even_arr.append(i)
            else:
                odd_arr.append(i)

        odd_arr.extend(even_arr)
        print(' '.join(str(i) for i in odd_arr))