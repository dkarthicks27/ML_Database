if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        if n % 2 == 0:
            even = arr[n//2:]
            even.reverse()
            odd = arr[:n//2]
        else:
            odd = arr[:n//2 + 1]
            even = arr[n//2+1:]
            even.reverse()

        new_arr = []
        x = 0
        y = 0
        for i in range(n):
            if i % 2 == 0:
                new_arr.append(odd[x])
                x += 1
            else:
                new_arr.append(even[y])
                y += 1

        print(' '.join(list(map(str, new_arr))))

